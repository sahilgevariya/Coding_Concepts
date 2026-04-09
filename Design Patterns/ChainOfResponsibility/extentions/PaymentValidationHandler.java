package ChainOfResponsibility.extentions;

import ChainOfResponsibility.abstraction.OrderHandler;
import ChainOfResponsibility.models.Order;
import ChainOfResponsibility.models.OrderResult;
import ChainOfResponsibility.models.OrderStatus;

import java.util.Set;

public class PaymentValidationHandler extends OrderHandler {

    private static final Set<String> SUPPORTED_METHODS = Set.of("CARD", "UPI", "WALLET");

    @Override
    public void handle(Order order, OrderResult result) {
        result.log("PaymentValidation: Validating payment method — " + order.paymentMethod());

        // Rule 1: Unsupported payment method
        if (!SUPPORTED_METHODS.contains(order.paymentMethod().toUpperCase())) {
            result.reject("Unsupported payment method: " + order.paymentMethod());
            result.log("PaymentValidation: ❌ REJECTED — unsupported method");
            return;
        }

        // Rule 2: UPI limit — max Rs.5000
        if ("UPI".equalsIgnoreCase(order.paymentMethod()) && order.amount() > 5000) {
            result.reject("UPI payment limit exceeded: max $5000, requested $" + order.amount());
            result.log("PaymentValidation: ❌ REJECTED — UPI limit exceeded");
            return;
        }

        result.setStatus(OrderStatus.PAYMENT_VALIDATED);
        result.log("PaymentValidation: ✅ PASSED");
        passToNext(order, result);
    }
}
