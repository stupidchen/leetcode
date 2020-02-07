package leetcode

func countSum(cur *TreeNode, sum *int, num int) {
	if cur == nil {
		return
	}
	var tmp = num * 10 + cur.Val
	if cur.Left == nil && cur.Right == nil {
		*sum = *sum + tmp
	}
	countSum(cur.Left, sum, tmp)
	countSum(cur.Right, sum, tmp)
}

func sumNumbers(root *TreeNode) int {
	var ret = 0
	countSum(root, &ret, 0)
	return ret
}