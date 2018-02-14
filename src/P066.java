import java.util.Arrays;

/**
 * Created by mike on 2/13/18.
 */
public class P066 {
    public int[] plusOne(int[] digits) {
        int i = digits.length - 1;
        digits[i] = digits[i] + 1;
        while (i > 0 && digits[i] >= 10) {
            digits[i] -= 10;
            digits[i - 1] += 1;
            i--;
        }

        int[] ret = digits;
        if (digits[i] >= 10) {
            ret = new int[digits.length + 1];
            ret[0] = 1;
            digits[i] -= 10;
            for (i = 0; i < digits.length; i++) ret[i + 1] = digits[i];
        }

        return ret;
    }
}
