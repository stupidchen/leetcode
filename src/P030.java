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
            for (int j = 0; j < n - lw; j += lw) {
                String word = s.substring(j, j + lw);
                Integer last = tacc.get(word);
                if (last == null || last == 0) {
                    tacc = (HashMap<String, Integer>) acc.clone();
                }
                else {
                    last--;
                    tacc.
                }
            }
        }
    }
}
