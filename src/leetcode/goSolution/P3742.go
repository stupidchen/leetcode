package goSolution

func flattenTree(node, prev *TreeNode) *TreeNode {
	if node == nil {
		return nil
	}
	if prev != nil {
		prev.Right = node
		prev.Left = nil
	}
	left, right := node.Left, node.Right
	lastLeft := node
	if left != nil {
		lastLeft = flattenTree(left, node)
	}
	if right != nil {
		lastRight := flattenTree(right, lastLeft)
		return lastRight
	}
	return lastLeft
}

func flatten(root *TreeNode)  {
	flattenTree(root, nil)
}
