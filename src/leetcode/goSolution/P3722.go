package goSolution

const MaxPowerOfThree = 1162261467

func isPowerOfThree(n int) bool {
	if n <= 0 || n > MaxPowerOfThree {
		return false
	}
	return MaxPowerOfThree % n == 0
}
