import java.util.Arrays;

/**
 * Created by mike on 2/13/18.
 */
public class P066 {
    public int[] plusOne(int[] digits) {
        int[] ret = Arrays.copyOf(digits, digits.length + 1);

        ret[0] = ret[0] + 1;
        int i = 0;
        while (ret[i] >= 10) {
            ret[i] -= 10;
            ret[i + 1] += 1;
            i++;
        }

        return ret;
    }
}
