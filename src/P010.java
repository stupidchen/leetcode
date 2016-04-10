/**
 * Created by mike on 4/9/16.
 */
public class P010 {
    public boolean isMatch(String s, String p) {
        if (s.length() == 0) return true;
        int ps = 0, pp = 0;

        int repeat = 0;
        while (pp < p.length()) {
            if (pp + 1 < p.length()) {
                if (p.charAt(pp + 1) == '*')
                    repeat = 1;
                else
                    repeat = 0;
            }
            if (p.charAt(pp) == '.') {
                if (repeat == 1)
                    return true;
                else
                    ps++;
            }
            else {
                if (repeat == 1) {
                    while ((ps < s.length()) && (s.charAt(ps) == p.charAt(pp))) ps++;
                }
                else {
                    if (s.charAt(ps) == p.charAt(pp))
                        ps++;
                    else
                        return false;
                }
            }
            if (ps == s.length()) break;
            pp += 1 + repeat;
        }

        if (ps == s.length()) return true;
        return false;
    }
}
