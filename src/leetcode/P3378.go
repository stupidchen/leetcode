package leetcode

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func levelOrderBottom(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}
	const maxdepth = 100
	const maxnum = 1000
	var queue [maxdepth * maxnum] *TreeNode
	var depth [maxdepth * maxnum] int

	queue[0] = root
	depth[0] = 0
	var t = 1
	for h := 0; h < t; h++ {
		if queue[h].Left != nil {
			queue[t] = queue[h].Left
			depth[t] = depth[h] + 1
			t++
		}
		if queue[h].Right != nil {
			queue[t] = queue[h].Right
			depth[t] = depth[h] + 1
			t++
		}
	}


	var ret = make([][] int, depth[t - 1] + 1)
	var m = depth[t - 1]
	t--
	for i := m; i >= 0; i-- {
		var num = 0
		for j := t; j >= 0 && depth[j] == depth[t]; j-- {
			num++
		}
		ret[m - i] =  make([] int, num)
		t -= num
		for j := 1; j <= num; j++ {
			ret[m - i][j - 1] = queue[j + t].Val
		}
	}

	return ret
}

