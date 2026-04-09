package Specification.specifications;

import Specification.interfaces.Specification;
import Specification.model.Product;

public record PriceRangeSpecification(double min, double max) implements Specification<Product> {

    public PriceRangeSpecification {
        if (min < 0 || max < 0)  throw new IllegalArgumentException("Price cannot be negative");
        if (min > max)           throw new IllegalArgumentException("min > max");
    }

    @Override
    public boolean isSatisfiedBy(Product p) {
        return p.price() >= min && p.price() <= max;
    }

    // Static factory for readability at call site
    public static PriceRangeSpecification between(double min, double max) {
        return new PriceRangeSpecification(min, max);
    }

    public static PriceRangeSpecification upTo(double max) {
        return new PriceRangeSpecification(0, max);
    }

    public static PriceRangeSpecification from(double min) {
        return new PriceRangeSpecification(min, Double.MAX_VALUE);
    }
}
