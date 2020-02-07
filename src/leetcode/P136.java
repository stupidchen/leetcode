/**
 * Created by mike on 3/3/18.
 */
public class P136 {
    public int singleNumber(int[] nums) {
        int n = nums.length;

        int ret = 0;
        for (int i = 0; i < n; i++) ret = ret ^ nums[i];

        return ret;
    }
}
