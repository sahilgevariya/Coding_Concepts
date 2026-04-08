package TemplateMethod.Impl;

import TemplateMethod.blueprint.ReportGenerator;

public class CsvReportGenerator extends ReportGenerator {
    @Override
    protected void fetchData() {
        System.out.println("Fetching data for CSV report...");
    }

    @Override
    protected void processData() {
        System.out.println("Processing data for CSV report...");
    }

    @Override
    protected void formatReport() {
        System.out.println("Formatting report as CSV...");
    }

    @Override
    protected void printReport() {
        System.out.println("Printing CSV report...\n");
    }
}

