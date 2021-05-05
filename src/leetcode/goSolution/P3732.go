package goSolution

func jump(nums []int) int {
	n := len(nums)
	q := []int{0}
	v := make([]int, n)
	v[0] = 1
	for h := 0; h < len(q); h++ {
		c := q[h]
		for i := 0; i < nums[c]; i++ {
			k := c + i + 1
			if k < n && v[k] == 0 {
				v[k] = v[c] + 1
				if k == n - 1 {
					h = len(q)
					break
				}
				q = append(q, k)
			}
		}
	}
	return v[n - 1] - 1
}