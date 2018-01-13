/**
 * Created by mike on 1/13/18.
 */
public class P053 {
    public int maxSubArray(int[] nums) {
        if (nums.length == 0) return 0;

        int t = nums[0], ans = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (t > 0)
                t += nums[i];
            else
                t = nums[i];
            if (t > ans) ans = t;
        }
        return ans;
    }
}
