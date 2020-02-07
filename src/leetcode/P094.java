import java.util.ArrayList;
import java.util.List;

/**
 * Created by mike on 3/8/18.
 */
public class P094 {
    private void solve(TreeNode now, List<Integer> ret) {
        if (now == null) return;
        solve(now.left, ret);
        ret.add(now.val);
        solve(now.right, ret);
    }

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> ret = new ArrayList<>();
        solve(root, ret);
        return ret;
    }
}
