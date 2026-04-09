package Specification.specifications;

import Specification.interfaces.Specification;
import Specification.model.Product;

public record MinRatingSpecification(double minRating) implements Specification<Product> {

    public MinRatingSpecification {
        if (minRating < 0.0 || minRating > 5.0)
            throw new IllegalArgumentException("Rating must be 0-5");
    }

    @Override
    public boolean isSatisfiedBy(Product item) {
        return item.rating() >= minRating;
    }

    public static MinRatingSpecification of(double minRating) {
        return new MinRatingSpecification(minRating);
    }
}
