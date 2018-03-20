import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by mike on 3/20/18.
 */
public class P093 {
    private HashSet<String> solutionsMap;

    private void solve(String str, String solution, int cur, int adn) {
        if (cur >= str.length() && adn == 4) {
            solutionsMap.add(solution);
            return;
        }
        if (cur >= str.length()) return;
        if (adn >= 4) return;

        for (int i = 1; i < 4; i++) {
            if (cur + i > str.length()) break;
            String ts = str.substring(cur, cur + i);
            int t = Integer.valueOf(ts);
            String tts = String.valueOf(t);
            if (!tts.equals(ts)) continue;
            if (adn != 0) ts = '.' + ts;
            if (t <= 255) solve(str, solution + ts, cur + i, adn + 1);
        }
    }

    public List<String> restoreIpAddresses(String s) {
        solutionsMap = new HashSet<>();
        solve(s, "", 0, 0);
        LinkedList<String> solutions = new LinkedList<>();
        solutions.addAll(solutionsMap);
        return solutions;
    }
}
