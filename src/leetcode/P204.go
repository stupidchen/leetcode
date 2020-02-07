package leetcode

var prime [10000000]bool
func countPrimes(n int) int {
	prime[0] = false
	prime[1] = false
	prime[2] = true
	for i := 2; i < n; i++ {
		prime[i] = true
	}

	var ans = 0
	for i := 2; i < n; i++ {
		if prime[i] {
			ans++
			for j := i * i; j < n; j += i {
				prime[j] = false
			}
		}
	}

	return ans
}
