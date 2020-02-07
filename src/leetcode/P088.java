/**
 * Created by mike on 1/29/18.
 */
public class P088 {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] tmp = new int[n + m];
        int i1 = 0, i2 = 0, i = 0;
        while (i1 < m && i2 < n) {
            if (nums1[i1] < nums2[i2]) {
                tmp[i++] = nums1[i1++];
            }
            else {
                tmp[i++] = nums2[i2++];
            }
        }
        while (i1 < m) tmp[i++] = nums1[i1++];
        while (i2 < n) tmp[i++] = nums2[i2++];

        while (i > 0) nums1[--i] = tmp[i];
    }
}
