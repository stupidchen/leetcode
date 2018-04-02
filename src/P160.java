/**
 * Created by mike on 4/2/18.
 */
public class P160 {
    private int getLength(ListNode head) {
        int len = 0;
        while (head != null) {
            len++;
            head = head.next;
        }
        return len;
    }
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int lenA = getLength(headA);
        int lenB = getLength(headB);
        while (lenA < lenB) {
            headB = headB.next;
            lenB--;
        }
        while (lenA > lenB) {
            headA = headA.next;
            lenA--;
        }
        while (headA != null) {
            if (headA == headB) return headA;
            headA = headA.next;
            headB = headB.next;
        }

        return null;
    }


    public static void main(String[] args) {
        P160 p = new P160();
        ListNode headA = new ListNode(5);
        headA.next = new ListNode(4);
        headA.next.next = new ListNode(6);
        headA.next.next.next = new ListNode(0);
        ListNode headB = new ListNode(9);
        headB.next = new ListNode(1);
        headB.next.next = headA.next;
        ListNode answer = p.getIntersectionNode(headA, headB);
        System.out.println(answer.val);
    }
}
