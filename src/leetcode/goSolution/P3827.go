package goSolution

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}
	if len(nums) == 1 {
		return &TreeNode{Val: nums[0]}
	}
	l, r := 0, len(nums)
	mid := (l + r) >> 1
	return &TreeNode{Val: nums[mid], Left: sortedArrayToBST(nums[0:mid]), Right: sortedArrayToBST(nums[mid+1:])}
}