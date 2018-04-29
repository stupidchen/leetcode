package leetcode

var solutions [10000][10000]int
var tmp [1000]int
var ansn int

func solvePathSum(cur *TreeNode, sum int, target int) {
	if cur == nil {
		return
	}

	sum += cur.Val
	tmp[0]++
	tmp[tmp[0]] = cur.Val
	if cur.Left == nil && cur.Right == nil {
		if sum == target {
			for i := 0; i <= tmp[0]; i++ {
				solutions[ansn][i] = tmp[i]
			}
			ansn++
		}
		tmp[0]--
		return
	}

	solvePathSum(cur.Left, sum, target)
	solvePathSum(cur.Right, sum, target)
	tmp[0]--
}

func pathSum(root *TreeNode, sum int) [][]int {
	ansn = 0
	tmp[0] = 0
	solvePathSum(root, 0, sum)
	var ret = make([][]int, ansn)
	for i := 0; i < ansn; i++ {
		ret[i] = solutions[i][1: solutions[i][0] + 1]
	}

	return ret
}
