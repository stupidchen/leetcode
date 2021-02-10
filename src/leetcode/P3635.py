class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None
        tmp = head
        nodes = {head: Node(head.val)}
        while tmp is not None:
            if tmp.next is not None and tmp.next not in nodes:
                nodes[tmp.next] = Node(tmp.next.val)
            if tmp.next is not None:
                nodes[tmp].next = nodes[tmp.next]
            if tmp.random is not None and tmp.random not in nodes:
                nodes[tmp.random] = Node(tmp.random.val)
            if tmp.random is not None:
                nodes[tmp].random = nodes[tmp.random]
            tmp = tmp.next
        return nodes[head]
