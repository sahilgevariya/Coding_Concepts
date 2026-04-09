package Specification.specifications;

import Specification.interfaces.Specification;
import Specification.model.Product;

public record MatchAllSpecification() implements Specification<Product> {

    @Override
    public boolean isSatisfiedBy(Product p) {
        return true;
    }

    // Static factory
    public static MatchAllSpecification get() {
        return new MatchAllSpecification();
    }
}