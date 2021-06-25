package goSolution

func findRedundantConnection(edges [][]int) []int {
	n := len(edges)
	for i, _ := range edges {
		edges[i][0]--
		edges[i][1]--
	}

	dsu := InitializeDSU(n)
	for i := n - 1; i >= 0; i-- {
		foundLoop := false
		for j := 0; j < n; j++ {
			if j != i {
				edge := edges[j]
				if dsu.FindSet(edge[0]) == dsu.FindSet(edge[1]) {
					foundLoop = true
					break
				}
				dsu.MergeSet(edge[0], edge[1])
			}

		}
		if !foundLoop {
			edges[i][0]++
			edges[i][1]++
			return edges[i]
		}
		dsu.Reset()
	}
	return nil
}
