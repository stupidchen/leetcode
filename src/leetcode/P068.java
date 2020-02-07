import java.util.LinkedList;
import java.util.List;

/**
 * Created by mike on 4/1/18.
 */
public class P068 {
    private String generateSpace(int n) {
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < n; i++) sb.append(' ');
        return sb.toString();
    }

    public List<String> fullJustify(String[] words, int maxWidth) {
        int n = words.length;
        int i = 0;
        List<String> ret = new LinkedList<>();
        while (i < n) {
            int l = words[i].length(), c = 1, m = 0;
            while (l <= maxWidth && i + c < n) {
                l += words[i + c].length() + 1;
                c++;
                m = 1;
            }
            String line = words[i];
            if (l > maxWidth) {
                l = 0;
                for (int j = i; j < i + c - m; j++) l += words[j].length();
                if (c - m > 1) {
                    int sp = (maxWidth - l) / (c - 1 - m), sm = (maxWidth - l) % (c - 1 - m);
                    for (int j = 1; j < c - m; j++) line += generateSpace(sp + (j <= sm ? 1 : 0)) + words[i + j];
                } else line += generateSpace(maxWidth - words[i].length());
                i = i + c - m;
            }
            else {
                for (int j = i + 1; j < n; j++) line += " " + words[j];
                line += generateSpace(maxWidth - l);
                i = n;
            }
            ret.add(line);
        }

        return ret;
    }

    public static void main(String[] args) {
        P068 p = new P068();
        p.fullJustify(new String[]{"what", "must", "be", "shall", "be."}, 12);
    }
}
