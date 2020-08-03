/**
 * Created by mike on 3/21/18.
 */
public class Solution {
    public boolean isPalindrome(String s) {
        int n = s.length();
        int l = 0;
        int r = n - 1;
        char[] a = s.toCharArray();

        while (l < r) {
            while (!(Character.isAlphabetic(a[l]) || Character.isDigit(a[l])) && l < r) l++;
            while (!(Character.isAlphabetic(a[r]) || Character.isDigit(a[r])) && l < r) r--;
            if (Character.toLowerCase(a[l]) != Character.toLowerCase(a[r])) return false;
            l++;r--;
        }

        return true;
    }
}
