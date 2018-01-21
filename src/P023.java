import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

/**
 * Created by mike on 1/22/18.
 */


public class P023 {
    public ListNode mergeKLists(ListNode[] lists) {
        Queue<ListNode> q = new PriorityQueue<>(new Comparator<ListNode>() {
            @Override
            public int compare(ListNode o1, ListNode o2) {
                return o1.val - o2.val;
            }
        });
        ListNode ret = null;
        for (ListNode t: lists) {
            if (t != null) q.add(t);
        }

        ListNode now = null;
        while (!q.isEmpty()) {
            ListNode t = q.peek();
            q.poll();
            if (t.next != null) q.add(t.next);
            if (ret == null) {
                ret = t;
                now = t;
            }
            else {
                now.next = t;
                now = t;
            }
        }

        return ret;
    }
}
