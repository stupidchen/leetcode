import java.util.regex.Pattern;

/**
 * Created by mike on 2/23/18.
 */
public class P065 {
    public boolean isNumber(String s) {
        if (s == null) return false;
        Pattern number = Pattern.compile("\\s*(\\+|-)?(\\d+(\\.\\d*)?|\\.\\d+)(e(\\+|-)?\\d+)?\\s*$");
        return number.matcher(s).matches();
    }

    public static void main(String[] args) {
        P065 p = new P065();
        System.out.println(p.isNumber("3e1.6"));
    }
}
