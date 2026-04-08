package Observer.Impls;

import Observer.interfaces.Observer;
import Observer.interfaces.Subject;

import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

public class Observable<T> implements Subject<T> {

    private final List<Observer<T>> observers = new CopyOnWriteArrayList<>();

    @Override
    public void subscribe(Observer<T> observer) {
        observers.add(observer);
    }

    @Override
    public void unsubscribe(Observer<T> observer) {
        observers.remove(observer);
    }

    @Override
    public void notifyObservers(T event) {
        observers.forEach(observer -> observer.update(event));
    }
}
