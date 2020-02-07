/**
 * Created by mike on 4/9/16.
 */
public class P008 {
    public int myAtoi(String str) {
        if (str.length() == 0) return 0;

        long isPositive = 1;
        long value = 0, t;
        int i = 0, ret;

        while ((str.charAt(i) == '-' || str.charAt(i) == '+' || str.charAt(i) == ' ') && (i < str.length())) {
            if (str.charAt(i) == '-') isPositive = -1;

            if (str.charAt(i) == '-' || str.charAt(i) == '+'){
                i++;
                break;
            }
            i++;
        }
        while (i < str.length()) {
            if (str.charAt(i) >= '0' && str.charAt(i) <= '9') {
                t = str.charAt(i) - '0';
            }
            else break;
            value = value * 10 + t;
            if (value >= Integer.MAX_VALUE || value <= Integer.MIN_VALUE) break;
            i++;
        }

        value *= isPositive;
        if (value >= Integer.MAX_VALUE) return Integer.MAX_VALUE;
        if (value <= Integer.MIN_VALUE) return Integer.MIN_VALUE;
        return (int)value;
    }
}
