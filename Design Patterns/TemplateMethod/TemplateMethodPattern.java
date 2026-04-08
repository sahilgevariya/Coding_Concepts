package TemplateMethod;

import TemplateMethod.Impl.CsvReportGenerator;
import TemplateMethod.Impl.ExcelReportGenerator;
import TemplateMethod.Impl.PdfReportGenerator;
import TemplateMethod.blueprint.ReportGenerator;

import java.util.List;
import java.util.concurrent.*;

/**
 * The Template Method pattern defines the skeleton of an algorithm in a method, deferring some steps to subclasses.
 *  It allows subclasses to redefine certain steps of an algorithm without changing the algorithm's structure.
 *
 * Real World Scenario {Report Generation System}
 *   Used by companies like Salesforce, SAP, Oracle in their reporting modules
 *
 * The Problem: Generate reports in PDF, CSV, Excel formats
 *   Every report follows same steps:
 *      Fetch Data
 *      Validate Data
 *      Format Data
 *      Build Report
 *      Save/Deliver Report
 *   But each format implements steps differently
 */
public class TemplateMethodPattern {
    public static void main(String[] args) throws InterruptedException {
        ReportGenerator pdfGenerator = new PdfReportGenerator();
        ReportGenerator csvGenerator = new CsvReportGenerator();
        ReportGenerator excelGenerator = new ExcelReportGenerator();

        ExecutorService executor = Executors.newFixedThreadPool(3);

        List<Callable<String>> tasks = List.of(
                () -> csvGenerator.generateReport(),
                () -> pdfGenerator.generateReport(),
                () -> excelGenerator.generateReport()
        );

        List<Future<String>> futures = executor.invokeAll(tasks);

        System.out.println("\n========== GENERATED REPORTS ==========");
        for (Future<String> future : futures) {
            try {
                System.out.println("✅ " + future.get());
            } catch (ExecutionException e) {
                System.err.println("❌ Report failed: " + e.getCause().getMessage());
            }
        }

        executor.shutdown();
        executor.awaitTermination(30, TimeUnit.SECONDS);
        System.out.println("========================================\n");
    }
}

