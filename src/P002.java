import java.math.BigInteger;
import java.util.List;

public class P002 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode lastL1 = null, result = l1;
        boolean nullL1 = (l1 == null);
        int valL2, k = 0;
        while ((l1 != null) || (l2 != null) || (k != 0)) {
            if (l1 == null) {
                l1 = new ListNode(0);
                if (nullL1) {
                    result = l1;
                    nullL1 = false;
                }
                if (lastL1 != null) lastL1.next = l1;
            }

            if (l2 == null) {
                valL2 = 0;
            }
            else{
                valL2 = l2.val;
                l2 = l2.next;
            }

            l1.val = l1.val + valL2 + k;
            if (l1.val > 9) {
                k = 1;
                l1.val -= 10;
            }
            else k = 0;

            lastL1 = l1;
            l1 = l1.next;
        }
        return result;
    }
}
