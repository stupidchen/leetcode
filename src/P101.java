/**
 * Created by mike on 2/17/18.
 */
public class P101 {
    public boolean isSymmetricRecursive(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) return true;
        if (root1 == null || root2 == null) return false;
        if (root1.val != root2.val) return false;
        return isSymmetricRecursive(root1.left, root2.right) && isSymmetricRecursive(root1.right, root2.left);
    }
    public boolean isSymmetric(TreeNode root) {
        return isSymmetricRecursive(root, root);
    }
}
