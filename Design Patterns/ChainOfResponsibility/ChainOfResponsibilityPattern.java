package ChainOfResponsibility;

import ChainOfResponsibility.models.Order;
import ChainOfResponsibility.models.OrderResult;
import ChainOfResponsibility.pipeline.OrderPipeline;

import java.util.List;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class ChainOfResponsibilityPattern {
    public static void main(String[] args) throws InterruptedException {
        var pipeline = OrderPipeline.getInstance();

        var orders = List.of(

                // ✅ Should PASS all checks — prime + wallet = 13% discount
                Order.of("CUST-001", "PROD-001", 5,  1500.0, "WALLET", "10.0.0.1",  true),

                // ❌ Should FAIL — blocked IP (fraud)
                Order.of("CUST-002", "PROD-001", 2,   500.0, "CARD",  "192.168.1.100", false),

                // ❌ Should FAIL — out of stock (PROD-002)
                Order.of("CUST-003", "PROD-002", 1,   300.0, "UPI",   "10.0.0.2",  false),

                // ❌ Should FAIL — UPI limit exceeded
                Order.of("CUST-004", "PROD-003", 3,  6000.0, "UPI",   "10.0.0.3",  false),

                // ✅ Should PASS — bulk(15 qty) + prime = 15% discount
                Order.of("CUST-005", "PROD-003", 15, 3000.0, "CARD",  "10.0.0.4",  true)
        );

        // Thread Safety Demo — concurrent order processing
        var executor = Executors.newFixedThreadPool(5);

        orders.forEach(order ->
                executor.submit(() -> {
                    OrderResult result = pipeline.process(order);
                    printResult(result);
                })
        );

        executor.shutdown();
        executor.awaitTermination(30, TimeUnit.SECONDS);
    }

    private static void printResult(OrderResult result) {
        var separator = "─".repeat(60);
        System.out.println(separator);
        System.out.println(result);
        System.out.println(separator + "\n");
    }
}

