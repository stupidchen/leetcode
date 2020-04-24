class ListNode:
    def __init__(self, key, val, next=None, last=None):
        self.key = key
        self.val = val
        self.next = next
        self.last = last


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = {}
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = self.head

    def _set_next_node(self, node, target):
        if target.next == node:
            return
        tn = target.next
        if tn:
            tn.last = node
        target.next = node
        nn = node.next
        if nn:
            nn.last = node.last
        else:
            self.tail = node.last
        node.last.next = nn
        node.last = target
        node.next = tn

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            self._set_next_node(self.map[key], self.head)
            return self.map[key].val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.map:
            self._set_next_node(self.map[key], self.head)
            self.map[key].val = value
        else:
            if self.capacity == 0:
                self.capacity = 1
                self.tail.last.next = None
                del self.map[self.tail.key]
                tmp = self.tail
                self.tail = self.tail.last
                del tmp
            node = ListNode(key, value, last=self.tail)
            self.map[key] = node
            self.tail.next = node
            self.tail = node
            self._set_next_node(node, self.head)
            self.capacity -= 1
