package goSolution

func minPartitions(n string) int {
	r := 0
	for _, c := range n {
		t := int(c) - 48
		if r < t {
			r = t
		}
	}
	return r
}
