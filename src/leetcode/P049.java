import java.util.*;

/**
 * Created by mike on 1/20/18.
 */

public class P049 {
    private int anagramHash(String str) {
        int[] t = new int[26];
        for (int i = 0; i < str.length(); i++) {
            t[str.charAt(i) - 'a']++;
        }
        int ret = 0, mod = 1283774121, p = 1;
        for (int i = 0; i < 26; i++) {
            ret = (ret + p * t[i]) % mod;
            p = (p * 17) % mod;
        }
        return ret;
    }
    public List<List<String>> groupAnagrams(String[] strs) {
        int n = strs.length;
        Map<Integer, List<String>> ansMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int hash = anagramHash(strs[i]);
            List<String> group = ansMap.get(hash);
            if (group == null) {
                group = new LinkedList<>();
                ansMap.put(hash, group);
            }
            group.add(strs[i]);
        }
        return new ArrayList<>(ansMap.values());
    }
    public static void main(String[] args) {
        P049 p = new P049();
        List<List<String>> ans = p.groupAnagrams(new String[]{"eat","tea","tan","ate","nat","bat"});
    }
}
