/**
 * Created by mike on 4/9/16.
 */
public class P009 {
    public static class Solution {
        public boolean isPalindrome(int x) {
            if (x < 0) return false;
            if (x == 0) return true;

            int i;
            for (i = 1; (long)i * (10) < Integer.MAX_VALUE; i *= 10) {
                if (i * 10 > x) break;
            }

            int t = x;
            while (x > 0) {
                if (((t / i) % 10) != (x % 10)) return false;
                i /= 10;
                x /= 10;
            }
            return true;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.isPalindrome(1874994781);
    }
}
