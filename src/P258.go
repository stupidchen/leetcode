package leetcode

func addDigits(num int) int {
	if num % 9 == 0 {
		if num == 0 {
			return 0
		}
		return 9
	} else {
		return num % 9
	}
}
