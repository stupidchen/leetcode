import java.lang.Math;
import java.util.HashMap;

public class P003 {
    public int lengthOfLongestSubstring(String s) {
        HashMap hashMap = new HashMap(100);
        int i = 0, j = 0, len = s.length();
        int result = 0;

        while (i < len) {
            while (j < len && !hashMap.containsKey(s.charAt(j))) {
                hashMap.put(s.charAt(j), s.charAt(j));
                j++;
            }
            result = Math.max(result, j - i);
            hashMap.remove(s.charAt(i));
            i++;
        }

        return result;
    }
}