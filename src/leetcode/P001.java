import java.lang.System;
import java.util.Scanner;

public class P001 {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];

        int len = nums.length;
        int t;
        for (int i = 0; i < len; i++) {
            t = target - nums[i];
            for (int j = i + 1; j < len; j++)
                if ((t ^ nums[j]) == 0) {
                    result[0] = i;
                    result[1] = j;
                    return result;
                }
        }

        return result;
    }
    public static void main(String[] args) {
        P001 p001 = new P001();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = scanner.nextInt();
        int t = scanner.nextInt();
        int[] r = p001.twoSum(a, t);
        System.out.printf("%d %d\n", r[0], r[1]);
    }
}