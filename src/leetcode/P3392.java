/**
 * Created by mike on 1/11/18.
 */
public class Solution {
    private double pow(double x, long n) {
        if (n == 0) return 1.0d;
        double t = pow(x, n >> 1);
        t *= t;
        if ((n & 1) == 1) t *= x;
        return t;
    }
    public double myPow(double x, int n) {
        if (x == 0) return 0;
        if (n < 0)
            return 1 / pow(x, 0L - (long) n);
        else
            return pow(x, n);
    }
}
