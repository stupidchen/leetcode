/**
 * Created by mike on 3/11/18.
 */
public class P798 {
    class TreeNode {
        TreeNode ls, rs;
        int l, r;
        int s;

        TreeNode(int l, int r) {
            this.l = l;
            this.r = r;
            this.s = 0;
        }
    }

    private void addTreeNode(int l, int r, TreeNode cur) {
        if (cur.l == l && cur.r == r) {
            cur.s += 1;
            return;
        }
        int mid = (cur.l + cur.r) >> 1;
        if (cur.rs == null) cur.rs = new TreeNode(mid + 1, cur.r);
        if (cur.ls == null) cur.ls = new TreeNode(cur.l, mid);
        if (l > mid) {
            addTreeNode(l, r, cur.rs);
            return;
        }
        if (r <= mid) {
            addTreeNode(l, r, cur.ls);
            return;
        }
        addTreeNode(l, mid, cur.ls);
        addTreeNode(mid + 1, r, cur.rs);
    }

    private int query(int x, TreeNode cur) {
        if (cur == null) return 0;
        if (cur.ls == null && cur.rs == null) return cur.s;
        int mid = (cur.l + cur.r) >> 1;
        if (x > mid)
            return query(x, cur.rs) + cur.s;
        else
            return query(x, cur.ls) + cur.s;
    }


    public int bestRotation(int[] A) {
        int n = A.length;
        int[] f = new int[n];
        TreeNode root = new TreeNode(0, n);
        for (int i = 0; i < n; i++) {
            int t = A[i];
            if (i >= t) addTreeNode(0, i - t, root);
            if (n + i - A[i] >= n)
                t = n - 1;
            else
                t = n + i - A[i];
            if (i + 1 <= t) addTreeNode(i + 1, t, root);
        }

        int ans = 0, max = 0;
        for (int i = 0; i < n; i++) {
            int t = query(i, root);
            if (t > max) {
                max = t;
                ans = i;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        P798 p = new P798();
        System.out.println(p.bestRotation(new int[]{1, 3, 0, 2, 4}));
    }
}
