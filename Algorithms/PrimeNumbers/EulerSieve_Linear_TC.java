import java.util.*;

// TC : O(n)
// SC : O(n)
public class EulerSieve_Linear_TC {
    public static void main(String[] args) {
        int n = 50;

        boolean[] isComposite = new boolean[n + 1];
        int[] primes = new int[n]; // upper bound: number of primes < n
        int pc = 0;

        for (int i = 2; i <= n; i++) {
            if (!isComposite[i]) primes[pc++] = i;

            for (int j = 0; j < pc; j++) {
                int p = primes[j];
                long x = (long) i * p;
                if (x > n) break;

                isComposite[(int) x] = true;

                // ensure each composite is marked once (by its smallest prime factor)
                if (i % p == 0) break;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < pc; i++) {
            sb.append(primes[i]).append(' ');
        }
        System.out.print(sb.toString().trim());
    }
}