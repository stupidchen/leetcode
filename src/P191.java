import java.lang.System;
import java.util.Scanner;

public class P191 {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int result = 0;
        while (n != 0) {
            int t = (n & (n ^ (n - 1)));
            result++;
            n -= t;
        }
        return result;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        P191 p191 = new P191();
        System.out.println(p191.hammingWeight(n));
    }
}