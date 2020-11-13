class Solution:
    def __add_new_node(self, queue, tail, new_node, depth):
        if new_node is not None:
            queue.append((new_node, depth))
            return tail + 1
        return tail

    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        queue = [(root, 0)]
        h = 0
        t = 0
        while h <= t:
            this, depth = queue[h]
            if h < t and queue[h + 1][1] == depth:
                this.next = queue[h + 1][0]

            t = self.__add_new_node(queue, t, this.left, depth + 1)
            t = self.__add_new_node(queue, t, this.right, depth + 1)

            h += 1
        return root
