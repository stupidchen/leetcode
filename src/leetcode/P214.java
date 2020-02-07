/**
 * Created by mike on 11/10/18.
 */
public class P214 {
    public String shortestPalindrome(String s) {
        String rs = new StringBuffer(s).reverse().toString();
        for (int i = s.length(); i > 0; i--) {
            if (rs.endsWith(s.substring(0, i))) {
                return new StringBuffer(s.substring(i)).reverse().toString() + s;
            }
        }
        return "";
    }
}

