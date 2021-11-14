# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        current = head
        n = 1
        while current is not None:
            c = 0
            temp = current
            last_node = None
            for i in range(n):
                if temp is not None:
                    c += 1
                    last = temp
                    temp = temp.next
                    if c == n:
                        break
                else:
                    break
            if c & 1 == 1:
                last_tail = last
                current = temp
            else:
                last = None
                first = current
                for i in range(n):
                    next_node = current.next
                    current.next = last
                    last = current
                    current = next_node
                    if current is None:
                        break
                first.next = next_node
                if last_tail is not None:
                    last_tail.next = last
                last_tail = first

            n += 1
        return head


if __name__ == '__main__':
    a = ListNode(1,
                 ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
    t = Solution().reverseEvenLengthGroups(a)
    print(t.val)

