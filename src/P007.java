import java.lang.*;
import java.lang.Integer;
import java.lang.Long;
import java.lang.String;
import java.lang.StringBuffer;
import java.lang.System;

public class P007 {
    public int reverse(int x) {
        long result = 0;

        while (x > 0) {
            result = result * 10 + x % 10;
            if (result > Integer.MAX_VALUE || result < Integer.MIN_VALUE) return 0;
        }

        return (int)result;
    }
}