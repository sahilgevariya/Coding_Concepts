package ResourcePool.abstraction;

import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.Supplier;

/**
 * A thread-safe, generic resource pool implementation.
 * It supports lazy creation of resources up to a specified maximum size.
 *
 * Two ways:
 *   1. `abstract` class with abstract `create()` method for resource creation.
 *   2. Constructor accepts a `Supplier<T>` for resource creation (more flexible, JAVA 8+).
 *
 * @param <T> The type of resource being pooled.
 */
public class ResourcePool<T> {
    // --------  ConcurrentLinkedQueue vs LinkedBlockingQueue  --------------
    private final ConcurrentLinkedQueue<T> pool = new ConcurrentLinkedQueue<>();
    private final Semaphore semaphore;
    private final AtomicInteger createdCount = new AtomicInteger(0);
//    private final ReentrantLock createLock = new ReentrantLock();

    private final int minSize, maxSize;
    private final Supplier<T> creator;

    private final ScheduledExecutorService cleaner =
            Executors.newSingleThreadScheduledExecutor(
                    // to create background thread for eviction without blocking main threads
//                    r -> {
//                Thread t = new Thread(r, "pool-eviction-thread");
//                t.setDaemon(true);  // won't block JVM shutdown
//                return t;
//            }
            );

    public ResourcePool(int minSize, int maxSize, Supplier<T> creator) {
        this.minSize = minSize;
        this.maxSize = maxSize;
        this.creator = creator;
        this.semaphore = new Semaphore(maxSize);

        initMinPool();
        startCleaner();
    }

    private void initMinPool() {
        for (int i = 0; i < minSize; i++) {
            pool.offer(creator.get());
            createdCount.incrementAndGet();
        }
    }

    // Borrow resource (blocking)
    public T borrow() throws InterruptedException {
        semaphore.acquire(); // limit concurrency

        T resource = pool.poll();
        if (resource != null)   return resource;

        // Lazy creation (double-check)
        if (createdCount.get() < maxSize) {
            if (createdCount.incrementAndGet() <= maxSize)  return creator.get();
            else                                            createdCount.decrementAndGet();  // undo increase if we can't create
        }

        // fallback (should be rare, as semaphore should prevent this)
        while ((resource = pool.poll()) == null) {
            Thread.yield();
        }
        return resource;
    }

    // Borrow with timeout
    public T borrow(long timeout, TimeUnit unit) throws InterruptedException {
        if (!semaphore.tryAcquire(timeout, unit))
            throw new RuntimeException("Timeout: No resource available");

        T resource = pool.poll();
        if (resource != null)   return resource;

        if (createdCount.get() < maxSize) {
            if (createdCount.incrementAndGet() <= maxSize)  return creator.get();
            else                                            createdCount.decrementAndGet();
        }

        while ((resource = pool.poll()) == null) {
            Thread.yield();
        }
        return resource;
    }

    public void release(T resource) {
        if (resource == null) return;

        pool.offer(resource);
        semaphore.release();
    }

    public int available() {
        return pool.size();
    }

    public int created() {
        return createdCount.get();
    }

    // Cleaner: shrink pool to minSize
    private void startCleaner() {
        cleaner.scheduleAtFixedRate(() -> {
            while (createdCount.get() > minSize && pool.size() > minSize) {
                T res = pool.poll();
                if (res == null) break;

                createdCount.decrementAndGet();
                System.out.println("Evicted resource : " + res);
            }
        }, 30, 30, TimeUnit.SECONDS);
    }
}
