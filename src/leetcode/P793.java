/**
 * Created by mike on 3/4/18.
 */
public class P793 {
    private long f(long x) {
        long ret = 0;
        while (x != 0) {
            ret += x / 5L;
            x /= 5L;
        }
        return ret;
    }

    public int preimageSizeFZF(int K) {
        long k = K;
        long l = 0, r = 5L * Integer.MAX_VALUE, mid, t;
        boolean found = false;
        while (l <= r) {
            mid = (l + r) >> 1;
            t = f(mid);
            if (t == k) {
                found = true;
                break;
            }
            if (t > k)
                r = mid - 1;
            else
                l = mid + 1;
        }

        if (found) return 5;
        return 0;
    }

    public static void main(String[] args) {
        P793 p = new P793();
        System.out.println(p.preimageSizeFZF(156));
    }
}
