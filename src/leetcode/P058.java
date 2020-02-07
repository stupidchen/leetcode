/**
 * Created by mike on 1/23/18.
 */
public class P058 {
    public int lengthOfLastWord(String s) {
        if (s == null) return 0;
        String[] words = s.split(" ");
        if (words.length == 0) return 0;
        return words[words.length - 1].length();
    }
}
