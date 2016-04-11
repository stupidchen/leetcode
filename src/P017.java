import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by mike on 4/11/16.
 */
public class P017 {
    private Map digitMap;

    private void getCombinations(List ret, String digits, int now, String letters) {
        if (now == digits.length()) {
            ret.add(letters);
            return;
        }

        String str = (String)digitMap.get((int)digits.charAt(now) - 48);
        for (int i = 0; i < str.length(); i++)
            getCombinations(ret, digits, now + 1, letters + str.charAt(i));
    }
    public List<String> letterCombinations(String digits) {
        digitMap = new HashMap<Integer, String>();
        digitMap.put(Integer.valueOf(2), "abc");
        digitMap.put(Integer.valueOf(3), "def");
        digitMap.put(Integer.valueOf(4), "ghi");
        digitMap.put(Integer.valueOf(5), "jkl");
        digitMap.put(Integer.valueOf(6), "mno");
        digitMap.put(Integer.valueOf(7), "pqrs");
        digitMap.put(Integer.valueOf(8), "tuv");
        digitMap.put(Integer.valueOf(9), "wxyz");

        List ret = new ArrayList<String>();
        if (digits.length() == 0) return ret;
        getCombinations(ret, digits, 0, "");

        return ret;
    }
}
