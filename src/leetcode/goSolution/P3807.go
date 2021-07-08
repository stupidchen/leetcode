package goSolution

func findLength(nums1 []int, nums2 []int) int {
	n, m := len(nums1), len(nums2)
	f := Initialize2DIntSlice(n + 1, m + 1, 0)
	ret := 0
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if nums1[i] == nums2[j] {
				f[i + 1][j + 1] = f[i][j] + 1
				ret = max(f[i + 1][j + 1], ret)
			} else {
				f[i + 1][j + 1] = 0
			}
		}
	}
	return ret
}
