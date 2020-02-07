public class P326 {
    private static int maxThreePowerInt = 1162261467;
    public boolean isPowerOfThree(int n) {
        if ((n <= 0) || (n > maxThreePowerInt)) return false;
        return (maxThreePowerInt % n == 0);
    }
}