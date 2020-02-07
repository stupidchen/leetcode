/**
 * Created by mike on 2/8/18.
 */
public class P045 {
    public int jump(int[] nums) {
        int n = nums.length;
        if (n < 2) return 0;

        int[] f = new int[n];
        int ans;
        if (nums[0] >= n - 1)
            ans = 1;
        else {
            f[1] = nums[0];
            int i = 1;
            ans = -1;
            while (ans == -1 && i < n - 1) {
                for (int t = f[i - 1]; t <= f[i]; t++) {
                    if (t + nums[t] >= n - 1) {
                        ans = i + 1;
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
