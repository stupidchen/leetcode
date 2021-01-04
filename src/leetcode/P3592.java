/**
 * Created by mike on 4/14/16.
 */
public class Solution {
    private ListNode head, now;
    private void setNode(ListNode next) {
        if (head == null) head = next;
        if (now != null) now.next = next;
        now = next;
    }
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        while (l1 != null || l2 != null) {
            if (l1 == null || (l2 != null && l1.val > l2.val)) {
                setNode(l2);
                l2 = l2.next;
            }
            else {
                setNode(l1);
                l1 = l1.next;
            }
        }
        return head;
    }
}
