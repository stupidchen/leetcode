import java.util.ArrayList;
import java.util.List;

/**
 * Created by mike on 4/14/16.
 */
public class P022 {
    private int n;
    private void generateParenthesisRecursive(List result, String parStr, int now, int parVal) {
        if (now == n) {
            result.add(parStr);
            return;
        }
        if (n - now - 1 >= parVal + 1) generateParenthesisRecursive(result, parStr + "(", now + 1, parVal + 1);
        if (parVal > 0) generateParenthesisRecursive(result, parStr + ")", now + 1, parVal - 1);
    }
    public List<String> generateParenthesis(int n) {
        this.n = n << 1;
        List ret = new ArrayList<String>();
        if (n != 0) generateParenthesisRecursive(ret, "", 0, 0);
        return ret;
    }
}
