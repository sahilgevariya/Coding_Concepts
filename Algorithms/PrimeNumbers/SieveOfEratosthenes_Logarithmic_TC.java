import java.util.Scanner;

// TC : O(n log log n)
// SC : O(n)
public class SieveOfEratosthenes_Logarithmic_TC {
    public static void main(String[] args) {
        int n = 50;

        if (n < 2) return;

        boolean[] isComposite = new boolean[n + 1];
        isComposite[0] = true;
        isComposite[1] = true;

        for (int p = 2; (long) p * p <= n; p++) {
            if (!isComposite[p]) {                 // p is prime
                for (int k = p * p; k <= n; k += p) {
                    isComposite[k] = true;         // mark multiples
                }
            }
        }

        StringBuilder out = new StringBuilder();
        for (int i = 2; i <= n; i++) {
            if (!isComposite[i]) out.append(i).append(' ');
        }
        System.out.print(out.toString().trim());
    }
}