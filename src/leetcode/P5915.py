# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        a = []
        t = head
        while t is not None:
            a.append(t.val)
            t = t.next
        n = len(a)
        b = []
        for i in range(1, n - 1):
            if (a[i - 1] < a[i] and a[i] > a[i + 1]) or (a[i - 1] > a[i] and a[i] < a[i + 1]):
                b.append(i)
        if len(b) < 2:
            return [-1, -1]
        min_d = b[1] - b[0]
        max_d = b[-1] - b[0]
        for i in range(2, len(b)):
            min_d = min(min_d, b[i] - b[i - 1])
        return (min_d, max_d)
