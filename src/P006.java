/**
 * Created by mike on 4/9/16.
 */
public class P006 {
    public String convert(String s, int numRows) {
        if (numRows == 1) return s;

        StringBuffer ret = new StringBuffer(s);
        int seg1 = (numRows - 1) << 1, seg2 = 0;
        int t = 0;
        for (int i = 0; i < numRows; i++) {
            int j = i, k = 0;
            while (j < s.length()) {
                ret.setCharAt(t++, s.charAt(j));
                if (t == s.length()) return ret.toString();

                if ((k & 1) == 0 && seg1 == 0) k++;
                if ((k & 1) == 1 && seg2 == 0) k++;

                if ((k & 1) == 0)
                    j += seg1;

                else
                    j += seg2;

                k++;
            }
            seg1 -= 2;
            seg2 += 2;
        }

        return ret.toString();
    }
}
