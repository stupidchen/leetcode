/**
 * Created by mike on 1/10/18.
 */
public class P038 {
    private String generate(String x) {
        String ret = "";
        int t = 1;
        for (int i = 1; i < x.length(); i++) {
            if (x.charAt(i) != x.charAt(i - 1)) {
                ret = ret + String.valueOf(t) + x.charAt(i - 1);
                t = 0;
            }
            t++;
        }
        ret += String.valueOf(t) + x.charAt(x.length() - 1);
        return ret;
    }
    public String countAndSay(int n) {
        String ans = "1";
        for (int i = 2; i <= n; i++) {
            ans = generate(ans);
        }

        return ans;
    }
}
