/**
 * Created by mike on 3/30/18.
 */
public class Solution {
    private int findDepth(TreeNode current) {
        if (current == null) return 0;

        return Math.max(findDepth(current.left), findDepth(current.right)) + 1;
    }

    public int maxDepth(TreeNode root) {
        return findDepth(root);
    }
}
