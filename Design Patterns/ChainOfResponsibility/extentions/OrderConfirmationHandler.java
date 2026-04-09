package ChainOfResponsibility.extentions;

import ChainOfResponsibility.abstraction.OrderHandler;
import ChainOfResponsibility.models.Order;
import ChainOfResponsibility.models.OrderResult;
import ChainOfResponsibility.models.OrderStatus;

public class OrderConfirmationHandler extends OrderHandler {

    @Override
    public void handle(Order order, OrderResult result) {
        result.log("OrderConfirmation: Finalizing order...");

        // In production: persist to DB, send confirmation email, notify warehouse
        result.setStatus(OrderStatus.CONFIRMED);
        result.log(String.format(
                "OrderConfirmation: ✅ ORDER CONFIRMED — id=%s finalAmount=%.2f",
                order.orderId(), result.getFinalAmount()
        ));
    }
}
