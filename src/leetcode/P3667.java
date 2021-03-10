/**
 * Created by mike on 4/10/16.
 */
public class Solution {
    public String intToRoman(int num) {
        String[][] digit = new String[][]{
                {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"},
                {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"},
                {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"},
                {"", "M", "MM", "MMM"}
        };

        StringBuffer ret = new StringBuffer();
        ret.append(digit[3][num / 1000 % 10]);
        ret.append(digit[2][num / 100 % 10]);
        ret.append(digit[1][num / 10 % 10]);
        ret.append(digit[0][num % 10]);

        return ret.toString();
    }
}
