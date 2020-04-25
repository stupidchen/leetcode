/**
 * Created by mike on 2/9/18.
 */
public class P3310 {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        if (n < 2) return true;

        int[] f = new int[n];
        boolean ans;
        if (nums[0] >= n - 1)
            ans = true;
        else {
            f[1] = nums[0];
            int i = 1;
            ans = false;
            while (!ans && i < n - 1) {
                for (int t = f[i - 1]; t <= f[i]; t++) {
                    if (t + nums[t] >= n - 1) {
                        ans = true;
                        break;
                    }
                    if (t + nums[t] > f[i + 1]) f[i + 1] = t + nums[t];
                }
                i++;
            }
        }

        return ans;
    }
}