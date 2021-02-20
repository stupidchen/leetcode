import java.util.HashMap;
import java.util.Map;
import java.util.Properties;

/**
 * Created by mike on 4/10/16.
 */
public class Solution {
    public int romanToInt(String s) {
        Map digitValue = new HashMap<Character, Integer>();
        digitValue.put(Character.valueOf('I'), Integer.valueOf(1));
        digitValue.put(Character.valueOf('V'), Integer.valueOf(5));
        digitValue.put(Character.valueOf('X'), Integer.valueOf(10));
        digitValue.put(Character.valueOf('L'), Integer.valueOf(50));
        digitValue.put(Character.valueOf('C'), Integer.valueOf(100));
        digitValue.put(Character.valueOf('D'), Integer.valueOf(500));
        digitValue.put(Character.valueOf('M'), Integer.valueOf(1000));

        int n = s.length();
        if (n == 0)  return 0;

        int i = n - 1, ret = 0;
        while (i >= 0) {
            int valueThis = (Integer)digitValue.get(Character.valueOf(s.charAt(i)));
            int valueNext;
            if (i > 0)
                valueNext = (Integer)digitValue.get(Character.valueOf(s.charAt(i - 1)));
            else
                valueNext = Integer.MAX_VALUE;
            if (valueNext < valueThis) {
                ret += valueThis - valueNext;
                i--;
            }
            else ret += valueThis;
            i--;
        }

        return ret;
    }
}
