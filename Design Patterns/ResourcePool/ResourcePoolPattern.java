package ResourcePool;

import ResourcePool.abstraction.ResourcePool;

import java.util.concurrent.atomic.AtomicInteger;

public class ResourcePoolPattern {
    public static void main(String[] args) {
        AtomicInteger cnt = new AtomicInteger(0);
        ResourcePool<String> pool = new ResourcePool<>(2,5, () -> "Resource-" + cnt.getAndIncrement());

        Runnable task = () -> {
            try {
                String res = pool.borrow();
                System.out.println(Thread.currentThread().getName() + " got " + res);

                Thread.sleep(10000);

                pool.release(res);
            } catch (Exception e) {
                e.printStackTrace();
            }
        };

        for (int i = 0; i < 100; i++) {
            new Thread(task).start();
        }
    }
}

