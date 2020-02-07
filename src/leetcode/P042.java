/**
 * Created by mike on 2/7/18.
 */
public class P042 {
//    class Segment {
//        Segment l, r;
//        int value;
//
//        Segment() {
//            value = -1;
//            l = null;
//            r = null;
//        }
//    }
//
//    private Segment root = null;
//
//    private int queryRMQ(Segment segment, int ql, int qr, int tl, int tr) {
//        if (tl == ql && tr == qr) return segment.value;
//
//        int mid = (ql + qr) >> 1;
//
//        if (tl >= mid) return queryRMQ(segment.r, mid, qr, tl, tr);
//        if (tr < mid) return queryRMQ(segment.l, tl, mid, tl, tr);
//
//        int rl = queryRMQ(segment.l, tl, mid, tl, mid);
//        int rr = queryRMQ(segment.r, mid, qr, mid, tr);
//        return rl > rr ? rl : rr;
//    }
//
//    private int initSegment(int[] value, Segment segment, int ql, int qr) {
//        if (ql + 1 == qr) {
//            segment.value = value[ql];
//            return segment.value;
//        }
//
//        if (segment.l == null) segment.l = new Segment();
//        if (segment.r == null) segment.r = new Segment();
//
//        int mid = (ql + qr) >> 1;
//        int rl = initSegment(value, segment.l, ql, mid);
//        int rr = initSegment(value, segment.r, mid, qr);
//        segment.value = rl > rr ? rl : rr;
//        return segment.value;
//    }

    public int trap(int[] height) {
        int n = height.length;
        if (n < 2) return 0;
        int[] max = new int[n + 1];

        for (int i = n - 2; i >= 0; i--)
            max[i] = height[i + 1] > max[i + 1] ? height[i + 1] : max[i + 1];

        int last = 0, ans = 0;
        for (int i = 0; i < n; i++) {
            if (last > height[i] && max[i] > height[i]) {
                int t = last > max[i] ? max[i] : last;
                ans += t - height[i];
            }
            if (last < height[i])
                last = height[i];
        }

        return ans;
    }

    public static void main(String[] args) {
        P042 p = new P042();
        System.out.println(p.trap(new int[]{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}));
    }
}
