package ChainOfResponsibility.abstraction;

import ChainOfResponsibility.models.Order;
import ChainOfResponsibility.models.OrderResult;

import java.util.Optional;

public abstract class OrderHandler {
    // State
    private Optional<OrderHandler> next = Optional.empty();

    // chain builder
    public OrderHandler setNext(OrderHandler next) {
        this.next = Optional.of(next);
        return next;
    }

    /**
     * Handle the order — implement your logic here
     * Call passToNext(order, result) to continue chain
     */
    public abstract void handle(Order order, OrderResult result);

    /**
     * Pass to next handler if exists — otherwise chain ends
     */
    protected void passToNext(Order order, OrderResult result) {
        next.ifPresent(handler -> handler.handle(order, result));
    }

    protected boolean hasNext() {
        return next.isPresent();
    }
}
