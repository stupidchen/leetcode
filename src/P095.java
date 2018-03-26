import java.util.LinkedList;
import java.util.List;

/**
 * Created by mike on 3/26/18.
 */
public class P095 {
    private List<TreeNode> solve(int l, int r) {
        List<TreeNode> ret = new LinkedList<>();
        if (l > r) {
            ret.add(null);
            return ret;
        }

        for (int i = l; i <= r; i++) {
            List<TreeNode> left = solve(l, i - 1);
            List<TreeNode> right = solve(i + 1, r);
            for (TreeNode lnode: left)
                for (TreeNode rnode: right) {
                    TreeNode p = new TreeNode(i);
                    p.left = lnode;
                    p.right = rnode;
                    ret.add(p);
                }
        }

        return ret;
    }

    public List<TreeNode> generateTrees(int n) {
        if (n == 0) return new LinkedList();
        return solve(1, n);
    }

    public static void main(String[] args) {
        P095 p = new P095();
        p.generateTrees(3);
    }
}
