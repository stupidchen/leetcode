import java.lang.String;
import java.lang.System;
import java.util.Scanner;

public class Solution {
    private int[][] f;
    private int ansStart, ans;

    public String longestPalindrome(String s) {
        int n = s.length();
        if (n == 0) return s;

        if (new StringBuffer(s).reverse().toString().equals(s)) return s;
        ans = 1;
        ansStart = 0;
        f = new int[n][n];

        for (int i = n - 1; i >= 0; i--) {
            f[i][i] = 1;
            for (int j = i + 1; j < n; j++) {
                if ((j - i == 1 || f[i + 1][j - 1] != 0) && (s.charAt(i) == s.charAt(j))) {
                    f[i][j] = f[i + 1][j - 1] + 2;
                    if (f[i][j] > ans) {
                        ans = f[i][j];
                        ansStart = i;
                    }
                }
            }
        }

        return s.substring(ansStart, ansStart + ans);
    }
}