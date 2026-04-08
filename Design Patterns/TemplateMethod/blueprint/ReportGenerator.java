package TemplateMethod.blueprint;

public abstract class ReportGenerator {
    public String generateReport() {
        fetchData();
        processData();
        formatReport();
        printReport();
        return "Complete Report";
    }

    protected abstract void fetchData();

    protected abstract void processData();

    protected abstract void formatReport();

    protected abstract void printReport();

    // Hook method - required when not all child need to override it
    protected void encryptReport() {
        // default: no encryption
    }
}
