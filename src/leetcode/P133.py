# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None

        nodes = {}
        init_node = UndirectedGraphNode(node.label)
        self.cloneSubGrapth(node, init_node, nodes)
        return init_node

    def cloneSubGrapth(self, old_node, new_node, nodes):
        for node in old_node.neighbors:
            if node.label in nodes:
                new_node.neighbors.append(nodes[node.label])
            else:
                nextNode = UndirectedGraphNode(node.label)
                nodes[node.label] = nextNode
                new_node.neighbors.append(nextNode)
                self.cloneSubGrapth(node, nextNode, nodes)
