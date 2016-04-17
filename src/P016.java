import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by mike on 4/12/16.
 */
public class P016 {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);

        int ret = 0, minD = Integer.MAX_VALUE;

        int n = nums.length;

        for (int i = 0; i < n; i++)
            if (i == 0 || nums[i] != nums[i - 1]) {
                for (int j = i + 1; j < n; j++) {
                    if (j == i + 1 || nums[j] != nums[j - 1]) {
                        int t = target - nums[i] - nums[j];
                        int p = Arrays.binarySearch(nums, j + 1, n, t);
                        if (p >= 0) {
                            ret = target;
                            return ret;
                        }
                        else {
                            int d;
                            p = (-p) - 1;
                            if (p > j && p < n) {
                                d = target - (nums[p] + nums[i] + nums[j]);
                                if (minD > Math.abs(d)) {
                                    minD = Math.abs(d);
                                    ret = target - d;
                                }

                            }
                            if (p - 1 > j) {
                                d = target - (nums[p - 1] + nums[i] + nums[j]);
                                if (minD > Math.abs(d)) {
                                    minD = Math.abs(d);
                                    ret = target - d;
                                }
                            }
                            if (p + 1 < n) {
                                d = target - (nums[p + 1] + nums[i] + nums[j]);
                                if (minD > Math.abs(d)) {
                                    minD = Math.abs(d);
                                    ret = target - d;
                                }
                            }
                        }
                    }
                }
            }

        return ret;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = scanner.nextInt();
        P016 p016 = new P016();
        System.out.println(p016.threeSumClosest(a, 1));
    }
}
