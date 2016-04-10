/**
 * Created by mike on 4/10/16.
 */
public class P014 {
    public String longestCommonPrefix(String[] strs) {

        StringBuffer ret = new StringBuffer();

        int n = strs.length, m = Integer.MAX_VALUE, t = 0;

        if (n == 0) return ret.toString();

        for (int i = 0; i < n; i++)
            if (strs[i].length() < m) {
                t = i;
                m = strs[i].length();
            }

        for (int i = 0; i < m; i++) {
            boolean common = true;
            for (int j = 0; j < n; j++)
                if (strs[j].charAt(i) != strs[t].charAt(i)) {
                    common = false;
                    break;
                }
            if (common) {
                ret.append(strs[t].charAt(i));
            }
            else break;
        }

        return ret.toString();
    }
}
