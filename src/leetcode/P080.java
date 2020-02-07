import java.util.Arrays;

/**
 * Created by mike on 3/2/18.
 */
public class P080 {
    public int removeDuplicates(int[] nums) {
        if (nums == null) return 0;

        int n = nums.length;
        int[] tmp = Arrays.copyOf(nums, n);
        Arrays.sort(tmp);

        Integer last = null;
        int times = 0, ret = 0;
        for (int i = 0; i < n; i++) {
            if (last == null || last != tmp[i]) {
                times = 1;
                last = tmp[i];
            }
            else times++;

            if (times <= 2) nums[ret++] = tmp[i];
        }

        return ret;
    }
}
