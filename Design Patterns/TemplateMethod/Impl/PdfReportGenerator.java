package TemplateMethod.Impl;

import TemplateMethod.blueprint.ReportGenerator;

public class PdfReportGenerator extends ReportGenerator {
    @Override
    protected void fetchData() {
        System.out.println("Fetching data for Pdf report...");
    }

    @Override
    protected void processData() {
        System.out.println("Processing data for Pdf report...");
    }

    @Override
    protected void formatReport() {
        System.out.println("Formatting report as Pdf...");
    }

    @Override
    protected void printReport() {
        System.out.println("Printing Pdf report...\n");
    }
}
