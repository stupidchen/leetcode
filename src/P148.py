class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def len(self, head):
        ret = 0
        while head is not None:
            ret += 1
            head = head.next
        return ret

    def getitem(self, head, index):
        if index == 0:
            return head
        for i in range(index):
            if head is not None:
                head = head.next
            else:
                break
        return head

    def sort(self, head, len):
        if len <= 1:
            return head
        t = self.getitem(head, len >> 1)
        h1 = self.sort(head, len >> 1)
        h2 = self.sort(t, len - (len >> 1))
        l1 = 0
        l2 = 0
        th = ListNode(-1)
        ret = th
        for i in range(len):
            if l1 >= len >> 1:
                th.next = h2
                h2 = h2.next
                l2 += 1
            elif l2 >= len - (len >> 1):
                th.next = h1
                h1 = h1.next
                l1 += 1
            else:
                if h1.val < h2.val:
                    th.next = h1
                    h1 = h1.next
                    l1 += 1
                else:
                    th.next = h2
                    h2 = h2.next
                    l2 += 1
            th = th.next
        return ret.next

    def sortList(self, head):
        l = self.len(head)
        if l <= 1:
            return head
        ret = self.sort(head, l)
        t = self.getitem(ret, l - 1)
        t.next = None
        return ret


if __name__ == '__main__':
    a = [4, 2, 1, 3, -100]
    head = ListNode(-1)
    t = head
    for i in a:
        tmp = ListNode(i)
        t.next = tmp
        t = tmp
    head = Solution().sortList(head.next)
    p = []
    while head is not None:
        p.append(head.val)
        head = head.next
    print(p)
