package goSolution

func findPathSum(root *TreeNode, targetSum int, path []int, result *[][]int) {
	if root == nil {
		return
	}

	if root.Left == nil && root.Right == nil {
		if targetSum == root.Val {
			fPath := make([]int, len(path)+1)
			copy(fPath, path)
			fPath[len(path)] = root.Val
			*result = append(*result, fPath)
		}
		return
	}

	findPathSum(root.Left, targetSum - root.Val, append(path, root.Val), result)
	findPathSum(root.Right, targetSum - root.Val, append(path, root.Val), result)
}

func pathSum(root *TreeNode, targetSum int) [][]int {
	result := make([][]int, 0)
	findPathSum(root, targetSum, make([]int, 0), &result)
	return result
}
