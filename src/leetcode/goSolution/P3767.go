package goSolution

import "strconv"

func openLock(deadends []string, target string) int {
	lockSet := make(map[string]int)
	deadEndsSet := make(map[string]bool)
	for _, deadEnd := range deadends {
		deadEndsSet[deadEnd] = true
	}

	if target == "0000" {
		return 0
	}
	if deadEndsSet["0000"] {
		return -1
	}
	q := []string{"0000"}
	lockSet["0000"] = 0
	for h := 0; h < len(q); h++ {
		c := q[h]
		for i := 0; i < 4; i++ {
			n, _ := strconv.ParseInt(c[i:i+1], 10, 64)
			for j := -1; j < 2; j++ {
				if j != 0 {
					k := (int(n) + j) % 10
					if k < 0 {
						k = 9
					}
					t := c[:i] + strconv.Itoa(k) + c[i+1:]
					if t != "0000" && lockSet[t] == 0 && deadEndsSet[t] == false {
						lockSet[t] = lockSet[c] + 1
						q = append(q, t)
						if t == target {
							return lockSet[t]
						}
					}
				}
			}
		}
	}
	return -1
}
