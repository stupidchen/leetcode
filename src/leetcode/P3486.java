/**
 * Created by mike on 2/28/18.
 */
public class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) return null;

        int n = 1;
        ListNode tmp = head;
        while (tmp.next != null) {
            n++;
            tmp = tmp.next;
        }

        if (n == 1) return head;

        tmp.next = head;
        tmp = head;
        int m = 0;
        k = k % n;
        while (m != n - k - 1) {
            m++;
            tmp = tmp.next;
        }
        head = tmp.next;
        tmp.next = null;
        return head;
    }
}
