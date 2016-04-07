import java.lang.Math;
import java.util.Scanner;

public class P004 {
    public int findIndex(int[] nums1, int l1, int[] nums2, int l2, int index) {
        if (l1 >= nums1.length) return nums2[l2 + index - 1];
        if (l2 >= nums2.length) return nums1[l1 + index - 1];

        if (index == 1) return(Math.min(nums1[l1], nums2[l2]));

        int mid1 = Integer.MAX_VALUE;
        int mid2 = Integer.MAX_VALUE;
        if ((l1 + (index >> 1) - 1) < nums1.length) mid1 = nums1[l1 + (index >> 1) - 1];
        if ((l2 + (index >> 1) - 1) < nums2.length) mid2 = nums2[l2 + (index >> 1) - 1];

        if (mid1 < mid2)
            return findIndex(nums1, l1 + (index >> 1), nums2, l2, index - (index >> 1));
        else
            return findIndex(nums1, l1, nums2, l2 + (index >> 1), index - (index >> 1));
    }
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len1 = nums1.length;
        int len2 = nums2.length;

        double ret = (findIndex(nums1, 0, nums2, 0, (len1 + len2 + 1) / 2) + findIndex(nums1, 0, nums2, 0, (len1 + len2 + 2) / 2)) / 2.0;

        return ret;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int len1 = scanner.nextInt();
        int[] nums1 = new int[len1];
        for (int i = 0; i < len1; i++) nums1[i] = scanner.nextInt();
        int len2 = scanner.nextInt();
        int[] nums2 = new int[len2];
        for (int i = 0; i < len2; i++) nums2[i] = scanner.nextInt();

        P004 p004 = new P004();
        System.out.println(p004.findMedianSortedArrays(nums1, nums2));
    }
}