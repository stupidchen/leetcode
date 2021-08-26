public class Solution {
    private int point = 0;
    private boolean isValid(String[] node, int limit) {
        if (node[point].equals("#")) return true;
        if (point == limit - 1) return false;
        point++;
        if (!isValid(node, limit)) return false;
        if (point == limit - 1) return false;
        point++;
        if (!isValid(node, limit)) return false;
        return true;
    }
    public boolean isValidSerialization(String preorder) {
        String[] val = preorder.split(",");
        int n = val.length;
        if (n == 0) return true;
        return isValid(val, n) && (point == n - 1);
    }

}