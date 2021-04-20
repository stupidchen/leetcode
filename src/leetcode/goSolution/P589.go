package goSolution

/**
 * Definition for a Node.
 */
type Node struct {
    Val int
    Children []*Node
}

func preorder(root *Node) []int {
    ret := []int{}
    if root == nil {
        return ret
    }

    nodeStack := []*Node{}
    indexStack := []int{}

    nodeStack = append(nodeStack, root)
    indexStack = append(indexStack, 0)
    current := 0
    direction := 0
    for ; current >= 0; {
        if direction == 0 {
            ret = append(ret, nodeStack[current].Val)
        }

        if indexStack[current] < len(nodeStack[current].Children) {
            nodeStack = append(nodeStack, nodeStack[current].Children[indexStack[current]])
            indexStack = append(indexStack, 0)
            indexStack[current]++
            current++
            direction = 0
            continue
        }

        current--
        direction = 1
        sizeOfStack := len(indexStack)
        indexStack = indexStack[:sizeOfStack - 1]
        nodeStack = nodeStack[:sizeOfStack - 1]
    }
    return ret
}
