/**
 * Created by mike on 4/8/18.
 */
public class Solution {
    private ListNode getNextNode(ListNode node, int step) {
        for (int i = 0; i < step; i++) {
            if (node == null) return null;
            node = node.next;
        }
        return node;
    }

    public boolean hasCycle(ListNode head) {
        ListNode tmp1 = getNextNode(head, 1);
        ListNode tmp2 = getNextNode(head, 2);
        while (tmp1 != tmp2) {
            tmp1 = getNextNode(tmp1, 1);
            tmp2 = getNextNode(tmp2, 2);
        }

        if (tmp1 == null || tmp2 == null) return false;
        return true;
    }
}
