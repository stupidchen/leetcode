class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if head is None:
            return [None] * k
        ret = [ListNode() for i in range(k)]
        cur = [node for node in ret]
        cur_len = [0] * k
        t = head
        i = 0
        while t is not None:
            cur_len[i] += 1
            i = (i + 1) % k
            t = t.next
        t = head
        i = 0
        while t is not None:
            new = t
            sub = t.next
            if cur_len[i] == 0:
                i = i + 1
            cur_len[i] -= 1
            cur[i].next = new
            cur[i] = new
            new.next = None
            t = sub
        for i, node in enumerate(ret):
            ret[i] = node.next
        return ret
