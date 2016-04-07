import java.lang.System;
import java.util.Scanner;

public class P331 {
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

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        P331 test = new P331();
        System.out.println(test.isValidSerialization(scanner.nextLine()));
    }
}