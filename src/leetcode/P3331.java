import java.lang.SuppressWarnings;

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
public class P328 {
    public ListNode oddEvenList(ListNode head) {
        if (head == null) return null;

        ListNode firstEvenNode = head.next;
        ListNode lastOddNode = head;
        int i = 0;

        ListNode temp = head, now = head;
        while (now != null) {
            temp = now.next;
            if (now.next != null) now.next = (now.next).next;
            else now.next = null;
            if (((++i) & 1) == 1) lastOddNode = now;
            now = temp;
        }

        lastOddNode.next = firstEvenNode;

        return head;
    }
}