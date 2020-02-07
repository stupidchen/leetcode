import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by mike on 2/11/18.
 */


class Interval {
    int start;
    int end;
    Interval() { start = 0; end = 0; }
    Interval(int s, int e) { start = s; end = e; }
}
public class P056 {
    public List<Interval> merge(List<Interval> intervals) {
        Comparator<Interval> comparator = new Comparator<Interval>() {
            @Override
            public int compare(Interval o1, Interval o2) {
                if (o1.start != o2.start) return o1.start - o2.start;
                return o1.start - o2.start;
            }
        };

        List<Interval> ret = new LinkedList<>();
        if (intervals.size() == 0) return ret;

        Interval[] intervalsArray = new Interval[intervals.size()];
        intervals.toArray(intervalsArray);
        Arrays.sort(intervalsArray, comparator);

        Interval last = intervalsArray[0];
        for (int i = 1; i < intervalsArray.length; i++) {
            if (last.end < intervalsArray[i].start) {
                ret.add(last);
                last = intervalsArray[i];
            }
            else {
                if (intervalsArray[i].end > last.end) last.end = intervalsArray[i].end;
            }
        }
        ret.add(last);

        return ret;
    }
}
