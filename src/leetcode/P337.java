public class Solution {
    public int max(int x, int y){
        if (x > y) return x;
        return y;
    }

    public int calRob(TreeNode now, int ifRob){
        int result = 0;
        if (ifRob != 1){
            if (now.left != null) result += max(calRob(now.left, 1), calRob(now.left, 0));
            if (now.right != null) result += max(calRob(now.right, 1), calRob(now.right,0));
        }
        else{
            result = now.val;
            if (now.left != null) result += calRob(now.left, 0);
            if (now.right != null) result += calRob(now.right, 0);
        }
        return result;
    }
    public int rob(TreeNode root) {
        int robRoot = 0, robSon = 0;
        if (root != null){
            robRoot = calRob(root, 1);
            robSon = calRob(root, 0);
        }
        return max(robRoot, robSon);
    }
}