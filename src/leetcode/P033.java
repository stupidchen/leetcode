import java.util.Arrays;

/**
 * Created by mike on 1/16/18.
 */
public class P033 {
    public int search(int[] nums, int target) {
        int n = nums.length, i;
        if (n == 0) return -1;
        for (i = 0; i < n - 1; i++)
            if (nums[i] > nums[i + 1]) break;

        int l = Arrays.binarySearch(nums, i + 1, n, target);
        int r = Arrays.binarySearch(nums, 0, i + 1, target);
        if (l >= 0) return l;
        if (r >= 0) return r;
        return -1;
    }

    public static void main(String[] args) {
        P033 p = new P033();
        System.out.println(p.search(new int[]{5, 4}, 5));
    }
}
