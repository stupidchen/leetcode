package goSolution

func sumOfFlooredPairs(nums []int) int {
	m := max(nums...)
	b := make([]int, m + 1)
	for _, num := range nums {
		b[num] += 1
	}
	s := GetPrefixSum(b)
	ret := 0
	for _, num := range nums {
		if b[num] != 0 {
			t := m / num
			for j := 1; j <= t; j++ {
				k := s[min((j + 1) * num, m + 1)] - s[j * num]
				if k != 0 {
					k = (k * j * b[num]) % MODULO
					ret = (ret + k) % MODULO
				}
			}
			b[num] = 0
		}
	}
	return ret
}
