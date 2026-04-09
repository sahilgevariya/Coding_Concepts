package Specification.specifications;

import Specification.interfaces.Specification;
import Specification.model.Product;

public record DiscountSpecification(double percentage) implements Specification<Product> {
    public DiscountSpecification {
        if (percentage < 0.0 || percentage > 100.0)
            throw new IllegalArgumentException("Discount must be 0-100");
    }

    @Override
    public boolean isSatisfiedBy(Product p) {
        return p.discountPercent() >= percentage;
    }

    public static DiscountSpecification of(double percent) {
        return new DiscountSpecification(percent);
    }
}
