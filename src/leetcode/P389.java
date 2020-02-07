/**
 * Created by mike on 4/4/18.
 */
public class P389 {
    public char findTheDifference(String s, String t) {
        int[] f = new int[128];
        for (int i = 0; i < s.length(); i++) f[s.charAt(i)]++;
        for (int i = 0; i < t.length(); i++) f[t.charAt(i)]--;
        for (int i = 0; i < 128; i++)
            if (f[i] < 0) return (char)i;
        return 'a';
    }

    public static void main(String[] args) {
        P389 p = new P389();
        System.out.println(p.findTheDifference("abcd", "abcde"));
    }
}
