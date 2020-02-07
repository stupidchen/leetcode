import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by mike on 1/23/18.
 */
public class P030 {
    public List<Integer> findSubstring(String s, String[] words) {
        int m = words.length;
        int n = s.length();
        List<Integer> ret = new LinkedList<>();
        if (n == 0 || m == 0) return ret;

        HashMap<String, Integer> acc = new HashMap<>();
        for (String word: words) {
            Integer t = acc.get(word);
            if (t == null) t = 0;
            acc.put(word, ++t);
        }

        boolean[] can = new boolean[n];
        int lw = words[0].length();
        for (int i = 0; i < lw; i++) {
            HashMap<String, Integer> tacc = (HashMap<String, Integer>) acc.clone();
            int t = 0;
            for (int j = i; j <= n - lw; j += lw) {
                String word = s.substring(j, j + lw);
                Integer last = tacc.get(word);
                if (last == null) {
                    tacc = (HashMap<String, Integer>) acc.clone();
                    t = 0;
                }
                else {
                    if (last > 0) {
                        last--;
                        tacc.put(word, last);
                        t++;
                        if (t == m) {
                            can[j - (t - 1) * lw] = true;
                            String wordOfHead = s.substring(j - (t - 1) * lw, j - (t - 2) * lw);
                            tacc.put(wordOfHead, tacc.get(wordOfHead) + 1);
                            t--;
                        }
                    }
                    else {
                        while (last == 0) {
                            String wordOfHead = s.substring(j - t * lw, j - (t - 1) * lw);
                            tacc.put(wordOfHead, tacc.get(wordOfHead) + 1);
                            last = tacc.get(word);
                            t--;
                        }
                        last--;
                        tacc.put(word, last);
                        t++;
                    }
                }
            }
        }

        for (int i = 0; i < n; i++)
            if (can[i]) ret.add(i);
        return ret;
    }

    public static void main(String[] args) {
        P030 p = new P030();
        List<Integer> ans = p.findSubstring("aaaaa", new String[]{"aa", "aa"});
        System.out.println(ans);
    }
}
