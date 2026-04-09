package ChainOfResponsibility.extentions;

import ChainOfResponsibility.abstraction.OrderHandler;
import ChainOfResponsibility.models.Order;
import ChainOfResponsibility.models.OrderResult;
import ChainOfResponsibility.models.OrderStatus;

import java.util.Set;

public class FraudCheckHandler extends OrderHandler {

    // Simulating blocklisted IPs — in production: Redis/DB lookup
    private static final Set<String> BLOCKED_IPS = Set.of(
            "192.168.1.100", "10.0.0.50", "172.16.0.99"
    );

    private static final double MAX_SINGLE_ORDER_AMOUNT = 10_000.0;

    @Override
    public void handle(Order order, OrderResult result) {
        result.log("FraudCheck: Starting fraud detection...");

        // Rule 1: Blocked IP
        if (BLOCKED_IPS.contains(order.ipAddress())) {
            result.reject("Fraud detected: IP address is blocklisted — " + order.ipAddress());
            result.log("FraudCheck: ❌ REJECTED — blocked IP");
            return; // ← STOP chain
        }

        // Rule 2: Suspiciously high amount
        if (order.amount() > MAX_SINGLE_ORDER_AMOUNT) {
            result.reject("Fraud detected: Order amount exceeds limit — $" + order.amount());
            result.log("FraudCheck: ❌ REJECTED — amount too high");
            return;
        }

        // Rule 3: Suspiciously high quantity
        if (order.quantity() > 100) {
            result.reject("Fraud detected: Suspicious quantity — " + order.quantity());
            result.log("FraudCheck: ❌ REJECTED — suspicious quantity");
            return;
        }

        result.setStatus(OrderStatus.FRAUD_CHECKED);
        result.log("FraudCheck: ✅ PASSED");
        passToNext(order, result); // ← CONTINUE chain
    }
}
