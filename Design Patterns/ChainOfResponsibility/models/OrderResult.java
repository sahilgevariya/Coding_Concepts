package ChainOfResponsibility.models;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Mutable result object — carries state through chain
 * Thread safe — used within single thread pipeline
 */
public final class OrderResult {

    private final String          orderId;
    private       OrderStatus     status;
    private       double          finalAmount;    // amount after discounts
    private       String          rejectionReason;
    private final List<String> processingLog;  // audit trail
    private final LocalDateTime createdAt;

    public OrderResult(Order order) {
        this.orderId       = order.orderId();
        this.status        = OrderStatus.PENDING;
        this.finalAmount   = order.amount();
        this.processingLog = new ArrayList<>();
        this.createdAt     = LocalDateTime.now();
    }

    // Getters
    public String       getOrderId()         { return orderId; }
    public OrderStatus  getStatus()          { return status; }
    public double       getFinalAmount()     { return finalAmount; }
    public String       getRejectionReason() { return rejectionReason; }
    public List<String> getProcessingLog()   { return Collections.unmodifiableList(processingLog); }
    public LocalDateTime getCreatedAt()      { return createdAt; }
    public boolean      isRejected()         { return status == OrderStatus.REJECTED; }

    // Setters used by handlers
    public void setStatus(OrderStatus status)             { this.status = status; }
    public void setFinalAmount(double amount)             { this.finalAmount = amount; }
    public void reject(String reason) {
        this.status          = OrderStatus.REJECTED;
        this.rejectionReason = reason;
    }
    public void log(String message) {
        processingLog.add("[" + LocalDateTime.now() + "] " + message);
    }

    @Override
    public String toString() {
        return """
            OrderResult {
              orderId   : %s
              status    : %s
              amount    : %.2f
              reason    : %s
              log       : %s
            }""".formatted(orderId, status, finalAmount,
                rejectionReason != null ? rejectionReason : "N/A",
                processingLog);
    }
}
