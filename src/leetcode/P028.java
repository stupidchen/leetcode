public class P028 {
    public int strStr(String haystack, String needle) {
        int n = haystack.length();
        int m = needle.length();
        if (n < m) return -1;        
        if (n == 0 || m == 0) return 0;

        int[] next = new int[m];
        next[0] = -1;
        int j = -1;
        for (int i = 1; i < m; i++) {
            while (j >= 0 && needle.charAt(i) != needle.charAt(j + 1)) j = next[j];
            if (needle.charAt(i) == needle.charAt(j + 1)) j++;
            next[i] = j;
        }

        j = -1;
        for (int i = 0; i < n; i++) {
            while (j >= 0 && haystack.charAt(i) != needle.charAt(j + 1)) j = next[j];
            if (haystack.charAt(i) == needle.charAt(j + 1)) j++;
            if (j == m - 1) return i - m + 1;
        }

        return -1;
    }
}
