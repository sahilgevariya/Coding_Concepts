package ChainOfResponsibility.pipeline;

import ChainOfResponsibility.abstraction.OrderHandler;
import ChainOfResponsibility.extentions.*;
import ChainOfResponsibility.models.Order;
import ChainOfResponsibility.models.OrderResult;

public final class OrderPipeline {

    private final OrderHandler chain;

    // Singleton pipeline — chain built once, reused for all orders
    private static final OrderPipeline INSTANCE = new OrderPipeline();

    private OrderPipeline() {
        // Build the chain
        var fraudCheck   = new FraudCheckHandler();
        var inventory    = new InventoryCheckHandler();
        var payment      = new PaymentValidationHandler();
        var discount     = new DiscountHandler();
        var confirmation = new OrderConfirmationHandler();

        // Wire the chain
        fraudCheck
                .setNext(inventory)
                .setNext(payment)
                .setNext(discount)
                .setNext(confirmation);

        this.chain = fraudCheck;
    }

    public static OrderPipeline getInstance() {
        return INSTANCE;
    }

    public OrderResult process(Order order) {
        OrderResult result = new OrderResult(order);
        chain.handle(order, result);
        return result;
    }
}
