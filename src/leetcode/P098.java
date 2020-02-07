/**
 * Created by mike on 3/16/18.
 */
public class P098 {
    private boolean judge(TreeNode root, long l, long r) {
        if (root == null) return true;
        if (root.val <= l || root.val >= r) return false;

        if (root.left != null && root.left.val >= root.val) return false;
        if (root.right != null && root.right.val <= root.val) return false;
        return judge(root.left, l, root.val) && judge(root.right, root.val, r);
    }

    public boolean isValidBST(TreeNode root) {
        return judge(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
}
