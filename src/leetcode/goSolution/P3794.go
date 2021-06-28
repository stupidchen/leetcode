package goSolution

func removeDuplicates(s string) string {
	ret := make([]int32, 0)
	last := -1
	for _, c := range s {
		if last < 0 || ret[last] != c {
			last++
			if last < len(ret) {
				ret[last] = c
			} else {
				ret = append(ret, c)
			}
		} else {
			last -= 1
		}
	}

	retStr := ""
	for _, c := range ret[:last+1] {
		retStr += string(c)
	}
	return retStr
}
