package goSolution

func maxScore(cardPoints []int, k int) int {
	n := len(cardPoints)
	m := n - k
	s := GetPrefixSum(cardPoints)

	r := s[m]
	for i := m + 1; i <= n; i++ {
		r = min(r, s[i] - s[i - m])
	}
	r = s[n] - r
	return r
}
