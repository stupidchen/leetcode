/**
 * Created by mike on 1/27/18.
 */
public class P083 {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return null;
        ListNode lastNode = null, now = head;
        while (now != null) {
            if (lastNode != null && now.val == lastNode.val) {
                lastNode.next = now.next;
            }
            else
                lastNode = now;
            now = now.next;
        }
        return head;
    }
}
