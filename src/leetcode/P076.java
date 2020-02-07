/**
 * Created by mike on 3/25/18.
 */
public class P076 {
    public String minWindow(String s, String t) {
        int[] tchar = new int[128];
        int l = 0, ansl = -1, minlen = -1, count = 0, m = 0;

        for (int i = 0; i < t.length(); i++) {
            if (tchar[t.charAt(i)] == 0) m++;
            tchar[t.charAt(i)]++;
        }
        for (int i = 0; i < 128; i++)
            if (tchar[i] == 0) tchar[i] = Integer.MAX_VALUE;


        for (int i = 0; i < s.length(); i++) {
            tchar[s.charAt(i)]--;
            if (tchar[s.charAt(i)] == 0) count++;

            if (count == m) {
                while (l <= i) {
                    if (tchar[s.charAt(l)]++ == 0) {
                        count--;
                        break;
                    }
                    l++;
                }
                if (minlen == -1 || i - l + 1 < minlen) {
                    minlen = i - l + 1;
                    ansl = l;
                }
                l++;
            }
        }

        if (minlen == -1) return "";
        return s.substring(ansl, ansl + minlen);
    }

    public static void main(String[] args) {
        P076 p = new P076();
        System.out.println(p.minWindow("ADOBECODEBANC", "ABC"));
    }
}
