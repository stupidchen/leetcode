class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None
        tmp = head
        nodes = {head:RandomListNode(head.label)}
        while tmp is not None:
            if tmp.next is not None and tmp.next not in nodes:
                nodes[tmp.next] = RandomListNode(tmp.next.label)
            if tmp.next is not None:
                nodes[tmp].next = nodes[tmp.next]
            if tmp.random is not None and tmp.random not in nodes:
                nodes[tmp.random] = RandomListNode(tmp.random.label)
            if tmp.random is not None:
                nodes[tmp].random = nodes[tmp.random]
            tmp = tmp.next
        return nodes[head]
