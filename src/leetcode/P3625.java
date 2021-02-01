import java.lang.System;
import java.util.Scanner;

public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int result = 0;
        while (n != 0) {
            int t = (n & (n ^ (n - 1)));
            result++;
            n -= t;
        }
        return result;
    }
}