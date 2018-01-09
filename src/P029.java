import java.util.Scanner;

/**
 * Created by mike on 9/7/16.
 */
public class P029 {
    private int getMaxPow(long dividend, long divisor) {
        if (dividend < divisor) return -1;

        long temp;
        int pow = 0;
        do {
            temp = divisor << pow;
            pow++;
        } while (temp - dividend <= 0);
        return (pow - 2);
    }
    public int divide(int dividend, int divisor) {
        if (divisor == 0 || (dividend == Integer.MIN_VALUE && divisor == -1)) return Integer.MAX_VALUE;
        if (divisor == 1) return dividend;
        if (dividend == 0) return 0;

        int dividendSign = 1, divisorSign = 1;
        long tempDividend = dividend, tempDivisor = divisor;
        if (dividend < 0) {
            dividendSign = -1;
            tempDividend = -tempDividend;
        }
        if (divisor < 0) {
            divisorSign = -1;
            tempDivisor = -tempDivisor;
        }

        int result = 0;
        while (true) {
            int temp = getMaxPow(tempDividend, tempDivisor);
            if (temp < 0) break;
            result += 1 << temp;
            tempDividend -= tempDivisor << temp;
        }

        return result * dividendSign * divisorSign;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int dividend = scanner.nextInt();
        int divisor = scanner.nextInt();
        System.out.println(new P029().divide(dividend, divisor));
    }
}
