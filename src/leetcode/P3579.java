/**
 * Created by mike on 4/16/16.
 */

public class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null) return null;

        ListNode ret = head;
        if (head.next != null) ret = head.next;

        while (head != null && head.next != null) {
            ListNode nextNode = head.next.next;
            head.next.next = head;
            if (nextNode != null && nextNode.next != null)
                head.next = nextNode.next;
            else
                head.next = nextNode;
            head = nextNode;
        }

        return ret;
    }
}
