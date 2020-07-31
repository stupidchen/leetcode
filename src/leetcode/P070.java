public class Solution {
    public int climbStairs(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        if (n == 2) return 2;
        int t1 = 1, t2 = 2, t3 = 0, i;
        for (i = 3; i <= n; i++){
            t3 = t1 + t2;
            t1 = t2;
            t2 = t3;
        }
        return t3;
    }
}