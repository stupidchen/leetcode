package leetcode

func solveParitition(s string, index int, ans [][]string, sol []int) {
	
}

func partition(s string) [][]string {
	var ret = make([][]string, len(s), len(s))
	var sol = make([]int, len(s) + 1, len(s) + 1)
	solveParitition(s, 0, ret, sol)
	return ret
}