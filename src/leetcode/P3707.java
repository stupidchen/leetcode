/**
 * Created by mike on 3/10/18.
 */
public class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode cacheLast = null, cacheHead = null;
        ListNode last = null;
        ListNode tmp = head;
        while (tmp != null) {
            if (tmp.val >= x) {
                if (cacheHead == null)
                    cacheHead = tmp;
                else
                    cacheLast.next = tmp;
                cacheLast = tmp;
            }
            else {
                if (last == null)
                    head = tmp;
                else
                    last.next = tmp;
                last = tmp;
            }
            tmp = tmp.next;
        }
        if (cacheLast != null)
            cacheLast.next = null;
        if (last != null)
            last.next = cacheHead;
        else head = cacheHead;
        return head;
    }
}
