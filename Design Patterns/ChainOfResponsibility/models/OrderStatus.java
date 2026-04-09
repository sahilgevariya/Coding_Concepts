package ChainOfResponsibility.models;

public enum OrderStatus {
    PENDING,
    FRAUD_CHECKED,
    INVENTORY_CONFIRMED,
    PAYMENT_VALIDATED,
    DISCOUNT_APPLIED,
    CONFIRMED,
    REJECTED
}
