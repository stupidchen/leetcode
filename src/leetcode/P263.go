package leetcode

func isUgly(num int) bool {
	if num == 0 {
		return false
	}

	for i := 2; i <= 5; i++ {
		for ; num % i == 0; num /= i {

		}
	}

	return num == 1
}
