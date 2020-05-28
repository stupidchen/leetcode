import java.lang.Math;

public class Solution {
    public int[] countBits(int num) {
        int[] result = new int[num + 1];

        result[0] = 0;
        for (int i = 1; i <= num; i++) {
            result[i] = result[i - 1] - (int)(Math.log((i & (i ^ (i - 1))))/Math.log(2) - 1);
        }

        return result;
    }
}