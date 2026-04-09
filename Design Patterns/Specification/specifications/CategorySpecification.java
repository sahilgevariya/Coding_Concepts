package Specification.specifications;

import Specification.interfaces.Specification;
import Specification.model.Product;

import java.util.Arrays;
import java.util.Set;
import java.util.stream.Collectors;

public record CategorySpecification(Set<String> categories) implements Specification<Product> {

    // VarArgs constructor for convenience ex. new CategorySpecification("Electronics", "Books")
    public CategorySpecification(String... cats) {
         this(Arrays.stream(cats).map(String::toLowerCase).collect(Collectors.toSet()));
    }

    @Override
    public boolean isSatisfiedBy(Product product) {
        return categories.contains(product.category().toLowerCase());
    }

    // Static factory method for convenience ex. CategorySpecification.of("Electronics", "Books")
    public static CategorySpecification of(String... cats) {
        return new CategorySpecification(cats);
    }
}
