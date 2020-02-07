/**
 * Created by mike on 3/24/18.
 */
public class P099 {
    private TreeNode node0 = null, node1 = null, prev = new TreeNode(Integer.MIN_VALUE);

    private void findMistakeNodes(TreeNode cur) {
        if (cur == null) return;

        findMistakeNodes(cur.left);


        if (cur.val <= prev.val && node0 == null) node0 = prev;
        if (cur.val <= prev.val && node0 != null) node1 = cur;
        prev = cur;

        findMistakeNodes(cur.right);
    }

    public void recoverTree(TreeNode root) {
        findMistakeNodes(root);
        int t;
        t = node0.val;
        node0.val = node1.val;
        node1.val = t;
    }
}
