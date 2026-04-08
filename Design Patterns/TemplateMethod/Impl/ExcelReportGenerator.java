package TemplateMethod.Impl;

import TemplateMethod.blueprint.ReportGenerator;

public class ExcelReportGenerator extends ReportGenerator {
    @Override
    protected void fetchData() {
        System.out.println("Fetching data for Excel report...");
    }

    @Override
    protected void processData() {
        System.out.println("Processing data for Excel report...");
    }

    @Override
    protected void formatReport() {
        System.out.println("Formatting report as Excel...");
    }

    @Override
    protected void printReport() {
        System.out.println("Printing Excel report...\n");
    }
}

