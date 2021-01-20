import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Stack;

/**
 * Created by mike on 4/13/16.
 */
public class Solution {
    public boolean isValid(String s) {
        Stack charStack = new Stack<Character>();

        int n = s.length();
        if (n == 0) return true;
        if ((n & 1) == 1) return false;

        Map parMap = new HashMap<Character, Character>();
        parMap.put(')', '(');
        parMap.put('}', '{');
        parMap.put(']', '[');


        for (int i = 0; i < n; i++)
            if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[') {
                charStack.push(Character.valueOf(s.charAt(i)));
            }
            else {
                if (charStack.empty()) return false;
                char tempChar = (Character)charStack.pop();
                char leftPar = (Character)parMap.get(s.charAt(i));
                if (leftPar != tempChar) return false;
            }

        return (charStack.size() == 0);
    }
}
