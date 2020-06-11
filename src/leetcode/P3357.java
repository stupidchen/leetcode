/**
 * Created by mike on 2/24/18.
 */
public class Solution {
    public void sortColors(int[] nums) {
        int[] cn = new int[3];
        for (int i = 0; i < nums.length; i++) cn[nums[i]]++;

        int t = 0;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < cn[i]; j++) nums[t++] = i;
    }
}
