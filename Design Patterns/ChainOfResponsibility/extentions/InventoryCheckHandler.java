package ChainOfResponsibility.extentions;

import ChainOfResponsibility.abstraction.OrderHandler;
import ChainOfResponsibility.models.Order;
import ChainOfResponsibility.models.OrderResult;
import ChainOfResponsibility.models.OrderStatus;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class InventoryCheckHandler extends OrderHandler {

    // In production: call Inventory Service / DB
    // ConcurrentHashMap — thread safe for concurrent orders
    private static final Map<String, Integer> INVENTORY = new ConcurrentHashMap<>(Map.of(
            "PROD-001", 50,
            "PROD-002", 0,
            "PROD-003", 200,
            "PROD-004", 10
    ));

    @Override
    public void handle(Order order, OrderResult result) {
        result.log("InventoryCheck: Checking stock for product — " + order.productId());

        int available = INVENTORY.getOrDefault(order.productId(), 0);

        if (available < order.quantity()) {
            result.reject(String.format(
                    "Insufficient stock: requested=%d available=%d for product=%s",
                    order.quantity(), available, order.productId()
            ));
            result.log("InventoryCheck: ❌ REJECTED — insufficient stock");
            return;
        }

        result.setStatus(OrderStatus.INVENTORY_CONFIRMED);
        result.log(String.format("InventoryCheck: ✅ PASSED — stock available: %d", available));
        passToNext(order, result);
    }
}
