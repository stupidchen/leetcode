package goSolution

func groupMatchSticks(sticks []int, current int, groups []int, edge int) bool {
	if current >= len(sticks) {
		return true
	}

	stick := sticks[current]
	for i, v := range groups {
		if v + stick <= edge {
			groups[i] += stick
			if groupMatchSticks(sticks, current + 1, groups, edge) {
				return true
			}
			groups[i] -= stick
		}
	}

	return false
}

func makesquare(matchsticks []int) bool {
	s := sum(matchsticks)
	if s % 4 != 0 {
		return false
	}

	m := s / 4
	groups := make([]int, 4)
	return groupMatchSticks(matchsticks, 0, groups, m)
}
