/**
 * Created by mike on 4/11/16.
 */
public class Solution {
    public int maxArea(int[] height) {
        if (height.length <= 1) return 0;

        int ret = 0;
        int l = 0, r = height.length - 1;
        while (l < r) {
            ret = Math.max((r - l) * Math.min(height[l], height[r]), ret);
            if (height[r] > height[l]) {
                int t = l;
                while ((height[t] >= height[l]) && (l < r)) l++;
            }
            else {
                int t = r;
                while ((height[t] >= height[r]) && (l < r)) r--;
            }
        }

        return ret;
    }
}
