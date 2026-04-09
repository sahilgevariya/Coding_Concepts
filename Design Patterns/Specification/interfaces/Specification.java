package Specification.interfaces;

import Specification.specifications.DiscountSpecification;
import Specification.specifications.InStockSpecification;
import Specification.specifications.MinRatingSpecification;
import Specification.specifications.PriceRangeSpecification;

import java.util.List;

@FunctionalInterface
public interface Specification<T> {

    boolean isSatisfiedBy(T item);  // one method only

    default Specification<T> and(Specification<T> other) {
        // Java knows by target typing to create annonymous object of type Specification<T> as that's return type of method
        return item -> this.isSatisfiedBy(item) && other.isSatisfiedBy(item);

        // this is what actually happens under the hood, but it's more verbose.
//        return new Specification<T>() {
//            @Override
//            public boolean isSatisfiedBy(T item) {
//                return this.isSatisfiedBy(item) && other.isSatisfiedBy(item);
//            }
//        };
    }

    default Specification<T> or(Specification<T> other) {
        return item -> this.isSatisfiedBy(item) || other.isSatisfiedBy(item);
    }

    default Specification<T> not() {
        return item -> !this.isSatisfiedBy(item);
    }

    // get all items without any specification
    static <T> Specification<T> matchAll()  { return candidate -> true;  }
    static <T> Specification<T> matchNone()  { return candidate -> false;  }

    // combine list of specs with AND — reduces chaining noise
    static <T> Specification<T> allOf(List<Specification<T>> specs) {
        return specs.stream()
                .reduce(candidate -> true, Specification::and);
    }

    static <T> Specification<T> anyOf(List<Specification<T>> specs) {
        return specs.stream()
                .reduce(candidate -> false, Specification::or);
    }
}
