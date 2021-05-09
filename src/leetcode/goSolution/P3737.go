package goSolution


func isTargetValid(target []int) int {
	for _, v := range target {
		if v < 1 {
			return -1
		}
		if v != 1 {
			return 1
		}
	}

	return 0
}


func isPossible(target []int) bool {
	n := len(target)
	if n == 0 {
		return false
	}

	var t int
	for t = isTargetValid(target); t > 0; t = isTargetValid(target) {
		s := sum(target)
		m := max(target...)
		for i, v := range target {
			if v == m {
				k := s - m
				if k >= target[i] || k == 0 {
					return false
				}
				target[i] = (target[i] - 1) % k + 1
				break
			}
		}
	}

	return t == 0
}