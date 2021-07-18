/**
 * Created by mike on 1/22/18.
 */
public class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null) return null;

        ListNode ret = head;
        ListNode last = null;
        while (head != null) {
            int t = 0;
            ListNode now = head;
            while (now != null && t < k) {
                t++;
                now = now.next;
            }
            if (t == k) {
                now = head;
                t = 1;
                ListNode tmp, before = null;
                while (t < k) {
                    tmp = now.next;
                    now.next = before;
                    before = now;
                    now = tmp;
                    t++;
                }
                if (last == null)
                    ret = now;
                else
                    last.next = now;
                last = head;
                if (now != null) {
                    head = now.next;
                    now.next = before;
                }
            }
            else {
                if (last != null) last.next = head;
                break;
            }
        }

        return ret;
    }
}
