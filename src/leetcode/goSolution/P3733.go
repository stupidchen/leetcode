package goSolution

func arrayToBST(a []int) *TreeNode {
	var m = len(a)
	if m == 0 {
		return nil
	}
	if m == 1 {
		return &TreeNode{Val: a[0]}
	}

	var ret = TreeNode{Val: a[m >> 1]}
	ret.Left = arrayToBST(a[: m >> 1])
	ret.Right = arrayToBST(a[(m >> 1) + 1: ])
	return &ret
}

func sortedListToBST(head *ListNode) *TreeNode {
	var gen [100000]int
	var i = 0
	for tmp := head; tmp != nil; tmp = tmp.Next {
		gen[i] = tmp.Val
		i++
	}
	return arrayToBST(gen[:i])
}
