package ChainOfResponsibility.extentions;

import ChainOfResponsibility.abstraction.OrderHandler;
import ChainOfResponsibility.models.Order;
import ChainOfResponsibility.models.OrderResult;
import ChainOfResponsibility.models.OrderStatus;

public class DiscountHandler extends OrderHandler {

    private static final double PRIME_DISCOUNT     = 0.10; // 10%
    private static final double BULK_DISCOUNT      = 0.05; // 5%  (qty > 10)
    private static final double WALLET_CASHBACK    = 0.03; // 3%

    @Override
    public void handle(Order order, OrderResult result) {
        result.log("DiscountHandler: Calculating discounts...");

        double discount     = 0.0;
        double finalAmount  = order.amount();

        // Rule 1: Prime customer discount
        if (order.isPrimeCustomer()) {
            discount   += PRIME_DISCOUNT;
            result.log("DiscountHandler: Prime discount applied — 10%");
        }

        // Rule 2: Bulk order discount
        if (order.quantity() > 10) {
            discount   += BULK_DISCOUNT;
            result.log("DiscountHandler: Bulk discount applied — 5%");
        }

        // Rule 3: Wallet cashback
        if ("WALLET".equalsIgnoreCase(order.paymentMethod())) {
            discount   += WALLET_CASHBACK;
            result.log("DiscountHandler: Wallet cashback applied — 3%");
        }

        // Apply total discount
        finalAmount = finalAmount * (1 - discount);
        result.setFinalAmount(finalAmount);

        result.setStatus(OrderStatus.DISCOUNT_APPLIED);
        result.log(String.format(
                "DiscountHandler: ✅ Total discount=%.0f%% finalAmount=%.2f",
                discount * 100, finalAmount
        ));

        passToNext(order, result);
    }
}
