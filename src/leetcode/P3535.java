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

public class Solution {
    public List<Interval> _merge(List<Interval> intervals) {
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

    public int[][] merge(int[][] intervals)
    {
        List<Interval> a = new LinkedList<>();
        for (int i = 0; i < intervals.length; i++)
        {
            a.add(new Interval(intervals[i][0], intervals[i][1]));
        }

        List<Interval> r = this._merge(a);
        Interval[] intervalsArray = new Interval[r.size()];
        r.toArray(intervalsArray);
        int[][] ret = new int[r.size()][2];
        for (int i = 0; i < intervalsArray.length; i++)
        {
            ret[i][0] = intervalsArray[i].start;
            ret[i][1] = intervalsArray[i].end;
        }
        return ret;
    }
}
