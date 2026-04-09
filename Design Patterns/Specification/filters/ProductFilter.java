package Specification.filters;

import Specification.interfaces.Specification;
import Specification.model.Product;

import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public final class ProductFilter {
    private ProductFilter() {};

    public static List<Product> filter(List<Product> products, Specification<Product> specification) {
        return products.stream().filter(specification::isSatisfiedBy).toList();
    }

    public static Integer count(List<Product> products, Specification<Product> specification) {
        return (int) products.stream().filter(specification::isSatisfiedBy).count();
    }

    public static boolean exists(List<Product> products, Specification<Product> specification) {
        return products.stream().anyMatch(specification::isSatisfiedBy);
    }

    public static Map<String, List<Product>> groupByCategory(List<Product> products, Specification<Product> specification) {
        return products.stream().filter(specification::isSatisfiedBy).collect(Collectors.groupingBy(Product::category));
    }

    // More generic group by method
    public static <K> Map<K, List<Product>> groupBy(List<Product> products, Specification<Product> specification,
                                                    Function<Product, K> classifier) {  // Takes T -> returns K type
        return products.stream().filter(specification::isSatisfiedBy).collect(Collectors.groupingBy(classifier));
    }

}
