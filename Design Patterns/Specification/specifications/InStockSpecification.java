package Specification.specifications;

import Specification.interfaces.Specification;
import Specification.model.Product;

public record InStockSpecification(int requiredQuantity) implements Specification<Product> {

    public InStockSpecification {
        if (requiredQuantity < 0) throw new IllegalArgumentException("Required quantity cannot be negative");
    }

    // default: at least 1
    public InStockSpecification() {
        this(1);
    }

    @Override
    public boolean isSatisfiedBy(Product product) {
        return product.stockQuantity() >= requiredQuantity;
    }

    public static InStockSpecification of(int requiredQuantity) {
        return new InStockSpecification(requiredQuantity);
    }
}
