import java.util.LinkedList;
import java.util.List;

/**
 * Created by mike on 3/9/18.
 */
public class P089 {
    public List<Integer> grayCode(int n) {
        LinkedList<Integer> ret = new LinkedList<>();
        for (int i = 0; i < (1 << n); i++) ret.add(i ^ (i >> 1));
        return ret;
    }
}
