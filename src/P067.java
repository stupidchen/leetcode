/**
 * Created by mike on 2/20/18.
 */
public class P067 {
    public String addBinary(String a, String b) {
        if (b.length() > a.length()) {
            String t = a;
            a = b;
            b = t;
        }
        int la = a.length(), lb = b.length();
        for (int i = 0; i < la - lb; i ++) b = '0' + b;

        int k = 0;
        String c = "";
        for (int i = la - 1; i >= 0; i--) {
            int t = k + a.charAt(i) -  '0' + b.charAt(i) - '0';
            c = (char)((t & 1) + '0') + c;
            k = t >> 1;
        }
        if (k != 0) c = (char)(k + '0') + c;

        return c;
    }
}
