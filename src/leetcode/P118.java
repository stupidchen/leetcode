import java.util.LinkedList;
import java.util.List;

/**
 * Created by mike on 3/31/18.
 */
public class P118 {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ret = new LinkedList<>();
        if (numRows == 0) return ret;

        List<Integer> last = new LinkedList<>();
        last.add(1);

        for (int i = 0; i < numRows; i++) {
            ret.add(last);
            List<Integer> tmp = new LinkedList<>();
            for (int j = 0; j <= last.size(); j++) {
                int l = 0;
                if (j > 0) l = last.get(j - 1);
                int r = 0;
                if (j < last.size()) r = last.get(j);
                tmp.add(l + r);
            }
            last = tmp;
        }

        return ret;
    }

    public static void main(String[] args) {
        P118 p = new P118();
        p.generate(3);
    }
}
