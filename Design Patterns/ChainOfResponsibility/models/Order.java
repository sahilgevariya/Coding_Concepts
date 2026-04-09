package ChainOfResponsibility.models;

import java.util.UUID;

public record Order(
        String   orderId,
        String   customerId,
        String   productId,
        int      quantity,
        double   amount,
        String   paymentMethod,   // CARD, UPI, WALLET
        String   ipAddress,       // for fraud check
        boolean  isPrimeCustomer  // for discount
) {
    public Order {
        if (quantity <= 0)  throw new IllegalArgumentException("Quantity must be > 0");
        if (amount   <= 0)  throw new IllegalArgumentException("Amount must be > 0");
    }

    public static Order of(String customerId, String productId,
                           int quantity, double amount,
                           String paymentMethod, String ipAddress,
                           boolean isPrimeCustomer) {
        return new Order(
                UUID.randomUUID().toString(),
                customerId, productId,
                quantity, amount,
                paymentMethod, ipAddress,
                isPrimeCustomer
        );
    }
}