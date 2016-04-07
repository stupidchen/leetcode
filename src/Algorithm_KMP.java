import java.lang.String;
import java.lang.StringBuffer;
import java.lang.System;
import java.util.ArrayList;
import java.util.Scanner;

public class Algorithm_KMP {
    private String patternString, originString;
    private static Algorithm_KMP handle = new Algorithm_KMP();
    private int[] next;
    private ArrayList result;
    private boolean isUpdated;

    private Algorithm_KMP() {
        patternString = null;
        originString = null;
        result = null;
        next = null;
        isUpdated = true;
    }

    public static Algorithm_KMP getHandle() {
        return handle;
    }
    public void setPatternString(String str) {
        this.patternString = new String(str);
        isUpdated = true;
    }
    public String getPatternString(String str) {
        return this.patternString;
    }
    public void setOriginString(String str) {
        this.originString = new String(str);
        isUpdated = true;
    }
    public String getOriginString(String str) {
        return this.originString;
    }

    private void solveNext(String str) {
        int len = str.length();
        next = new int[len + 1];
        next[0] = -1;

        int i, j = -1;
        for (i = 1; i < len; i++) {
            while ((j >= 0) && (str.charAt(i) != str.charAt(j + 1))) j = next[j];
            if (str.charAt(i) == str.charAt(j + 1)) j++;
            next[i] = j;
        }
    }
    private void match() {
        if (patternString == null || originString == null || patternString.length() == 0 || originString.length() == 0) return;

        solveNext(patternString);
        result = new ArrayList();

        int i, j = -1;
        int n = originString.length();
        int m = patternString.length();

        for (i = 0; i < n; i++) {
            while ((j >= 0) && (originString.charAt(i) != patternString.charAt(j + 1))) j = next[j];
            if (originString.charAt(i) == patternString.charAt(j + 1)) j++;

            if (j == m - 1){
                result.add(i - m + 1);
                j = next[j];
            }
        }

        isUpdated = false;
    }

    public int getMatchCount() {
        if (isUpdated) match();

        return result.size();
    }
    public ArrayList getPositionList() {
        if (isUpdated) match();

        return result;
    }

    public static void main(String[] args) {
        Algorithm_KMP a = Algorithm_KMP.getHandle();

        Scanner scanner = new Scanner(System.in);
        int n;
        String str1, str2;

        n = scanner.nextInt();
        scanner.nextLine();

        for (int i = 0; i < n; i++) {
            str1 = scanner.nextLine();
            str2 = scanner.nextLine();

            a.setPatternString(str1);
            a.setOriginString(str2);

            System.out.println(a.getMatchCount());
        }
    }
}