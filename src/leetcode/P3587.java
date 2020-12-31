/**
 * Created by mike on 3/18/18.
 */
public class Solution {
    private int max(int x, int y) {
        if (x > y) return x;
        return y;
    }

    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        if (n == 0) return 0;

        int ret = 0, top = 0;
        int[] f = new int[n];
        for (int i = 0; i <= n; i++) {
            int h = i == n ? 0 : heights[i];
            if (top == 0 ||  heights[f[top - 1]] < h)
                f[top++] = i;
            else {
                int p = heights[f[--top]];
                int l = top == 0 ? i : i - (f[top - 1] + 1);
                ret = max(ret, l * p);
                i--;
            }
        }

        return ret;
    }
}
