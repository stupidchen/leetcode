import java.lang.String;
import java.lang.System;
import java.util.Scanner;

public class P005 {
    public String longestPalindrome(String s) {
        int len = s.length();

        if (len <= 1) return s;


        int[][] f = new int[len][len];
        int ansi = 0, ans = 0;

        for (int i = 0; i < len; i++)
            for (int j = 0; j < len; j++) {
                f[i][j] = 0;
                if (s.charAt(i) == s.charAt(len - j - 1)) {
                    if (i > 0 && j > 0 && f[i - 1][j - 1] + 1 > f[i][j]) f[i][j] = f[i - 1][j - 1] + 1;
                    else {
                        if (i == 0 || j == 0) f[i][j] = 1;
                    }
                }
                if (f[i][j] > ans) {
                    ans = f[i][j];
                    ansi = i;
                }
            }

        return s.substring(ansi - ans + 1, ansi + 1);
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.nextLine();
        P005 p005 = new P005();
        System.out.println(p005.longestPalindrome(str));
    }
}