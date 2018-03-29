/**
 * Created by mike on 3/29/18.
 */
public class P108 {
    private void solve(int[] nums, int l, int r, int cur, TreeNode node) {
        if (l <= cur - 1) {
            node.left = new TreeNode(nums[(l + cur - 1) >> 1]);
            solve(nums, l, cur - 1, (l + cur - 1) >> 1, node.left);
        }
        if (r >= cur + 1) {
            node.right = new TreeNode(nums[(cur + r + 1) >> 1]);
            solve(nums, cur + 1, r, (cur + r + 1) >> 1, node.right);
        }
    }

    public TreeNode sortedArrayToBST(int[] nums) {
        int n = nums.length;
        if (n == 0) return null;
        TreeNode root = new TreeNode(nums[(n - 1) >> 1]);
        solve(nums, 0, n - 1, (n - 1) >> 1, root);
        return root;
    }

    public static void main(String[] args) {
        P108 p = new P108();
        p.sortedArrayToBST(new int[]{-10, -3, 0, 5, 9});
    }
}
