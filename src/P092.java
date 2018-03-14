/**
 * Created by mike on 3/14/18.
 */
public class P092 {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode tmp = head, last = null;

        ListNode ll, lr, rl ,rr;
        for (int i = 0; i < m - 1; i++) {
            last = tmp;
            tmp = tmp.next;
        }
        ll = last;
        lr = tmp;

        last = tmp;
        tmp = tmp.next;
        for (int i = m; i < n; i++) {
            ListNode c = tmp.next;
            tmp.next = last;
            last = tmp;
            tmp = c;
        }
        rl = last;
        rr = tmp;

        lr.next = rr;
        if (ll != null) {
            ll.next = rl;
            return head;
        }
        else
            return rl;
    }
}
