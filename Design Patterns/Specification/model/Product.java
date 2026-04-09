package Specification.model;

public record Product(String id,
                      String name,
                      String category,
                      double price,
                      double rating,
                      int    stockQuantity,
                      double discountPercent,
                      boolean active) {
    // Compact constructor for validation
    public Product {
        if (price < 0)                                      throw new IllegalArgumentException("Price cannot be negative");
        if (rating < 0 || rating > 5)                       throw new IllegalArgumentException("Rating must be 0-5");
        if (discountPercent < 0 || discountPercent > 100)   throw new IllegalArgumentException("Invalid discount");
    }

    // Static factory methods — no builder needed
    public static Product of(String id, String name, String category,
                             double price, double rating,
                             int stock, double discount) {
        return new Product(id, name, category, price, rating, stock, discount, true);
    }

    @Override
    public String toString() {
        return """
            Product[id=%-6s name=%-20s category=%-10s \
            price=%7.2f rating=%.1f stock=%3d discount=%4.1f%%]\
            """.formatted(id, name, category, price, rating, stockQuantity, discountPercent);
    }
}
