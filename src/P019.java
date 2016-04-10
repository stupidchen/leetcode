/**
 * Created by mike on 4/10/16.
 */
public class P019 {
    private int remove(ListNode now, int number) {
        if (now == null) return -1;

        int t = remove(now.next, number) + 1;
        if (t == number) {
            if (now.next != null)
                now.next = now.next.next;
            else
                now.next = null;
        }

        return t;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode ret = head;
        if (remove(head, n) + 1 == n) ret = head.next;

        return ret;
    }
}
