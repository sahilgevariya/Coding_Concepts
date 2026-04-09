package Specification;

import Specification.filters.ProductFilter;
import Specification.interfaces.Specification;
import Specification.model.Product;
import Specification.specifications.*;

import java.util.List;

public class SpecificationPattern {
    public static void main(String[] args) {
        var catalog = List.of(
                Product.of("P001", "Samsung Galaxy S23", "MOBILE",  799.99, 4.5,  50, 10.0),
                Product.of("P002", "iPhone 15",          "MOBILE",  999.99, 4.8,  30,  35.0),
                Product.of("P003", "Redmi Note 12",      "MOBILE",  249.99, 4.2, 200, 20.0),
                Product.of("P004", "Dell XPS 15",        "LAPTOP", 1499.99, 4.7,  15,  8.0),
                Product.of("P005", "MacBook Pro",        "LAPTOP", 1999.99, 4.9,   0,  0.0),  // out of stock
                Product.of("P006", "Sony WH-1000XM5",   "AUDIO",   349.99, 4.6,  75, 15.0),
                Product.of("P007", "Boat Earphones",     "AUDIO",    49.99, 3.8, 500, 30.0),
                Product.of("P008", "iPad Pro",           "TABLET",  899.99, 4.7,   0,  0.0)   // out of stock
        );

        Specification<Product> audioProducts = CategorySpecification.of("Audio");
        System.out.println("Audio Products:");
        ProductFilter.filter(catalog, audioProducts).forEach(System.out::println);

        Specification<Product> budgetMobilesRules = CategorySpecification.of("Mobile")
                .and(PriceRangeSpecification.upTo(500.0))
                .and(MinRatingSpecification.of(4.0))
                .and(InStockSpecification.of(1));

        Integer budgetMobileCount = ProductFilter.count(catalog, budgetMobilesRules);
        System.out.println("\nBudget Mobile Count: " + budgetMobileCount);
        ProductFilter.filter(catalog, budgetMobilesRules).forEach(System.out::println);

        var flashSaleProductsRules = Specification.allOf(List.of(
                PriceRangeSpecification.upTo(1000.0),
                MinRatingSpecification.of(4.0),
                InStockSpecification.of(1),
                DiscountSpecification.of(25.0)
        ));
        System.out.println("\nFlash Sale Products:");
        ProductFilter.filter(catalog, flashSaleProductsRules).forEach(System.out::println);

        System.out.println("\nProducts grouped by category:");
        ProductFilter.groupBy(catalog, MatchAllSpecification.get(), Product::category)
                .forEach((category, products) -> {
                    System.out.println("\nCategory: " + category);
                    products.forEach(System.out::println);
                }
        );
    }
}

