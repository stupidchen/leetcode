import java.lang.System;
import java.util.Scanner;

public class P190 {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        return (-n - 1);
    }
    public static void main(String args[]) {
        P190 p190 = new P190();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(p190.reverseBits(n));
    }
}