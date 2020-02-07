/**
 * Created by mike on 3/7/18.
 */
public class P082 {
    public ListNode deleteDuplicates(ListNode head) {
        boolean dup = false;
        ListNode tmp = head, last = null;
        while (tmp != null) {
            if (tmp.next != null && tmp.next.val == tmp.val) {
                dup = true;
                if (last != null) last.next = tmp.next;
                if (tmp == head) head = tmp.next;
            }
            else {
                if (dup) {
                    if (last != null) last.next = tmp.next;
                    dup = false;
                    if (tmp == head) head = tmp.next;
                }
                else
                    last = tmp;
            }
            tmp = tmp.next;
        }
        return head;
    }
}
