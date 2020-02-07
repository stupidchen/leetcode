/**
 * Created by mike on 3/11/18.
 */
public class P796 {
    public String shift(String x, int y) {
        String ret = "";
        int m = x.length();
        for (int i = 0; i < m; i++) ret += x.charAt((y + i) % m);
        return ret;
    }
    public boolean rotateString(String A, String B) {
        for (int i = 0; i < A.length(); i++)
            if (shift(A, i).equals(B)) return true;
        return false;
    }
}
