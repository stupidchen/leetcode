public class P026 {
    public int removeDuplicates(int[] nums) {
        int ret = 0, lastSpace = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (i == n - 1 || nums[i] != nums[i + 1]) {
                ret++;
                nums[lastSpace++] = nums[i];
            }
        }
        return ret;
    }
}
