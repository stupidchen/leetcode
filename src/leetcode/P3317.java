import java.util.HashMap;
import java.util.Map;

/**
 * Created by mike on 1/28/18.
 */
public class P3317 {
    public int numJewelsInStones(String J, String S) {
        int n = S.length();
        int m = J.length();
        Map<Character, Boolean> jewels = new HashMap<>();
        for (int i = 0; i < m; i++) jewels.put(J.charAt(i), true);
        int ret = 0;
        for (int i = 0; i < n; i++)
            if (jewels.get(S.charAt(i)) != null) ret++;
        return ret;
    }
}
