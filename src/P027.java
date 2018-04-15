public class P027 {
    public int removeElement(int[] nums, int val) {
        int n = nums.length;
        int i = 0;
        while (i < n) {
            if (nums[i] == val) {
                for (int j = i; j < n - 1; j++) nums[j] = nums[j + 1];
                n--;
            }
            else i++;
        }
        return n;
    }
}
