package goSolution

import "sort"

func maxArea(h int, w int, horizontalCuts []int, verticalCuts []int) int {
	horizontalCuts = append(horizontalCuts, h)
	verticalCuts = append(verticalCuts, w)
	sort.Slice(horizontalCuts, func(i, j int) bool {
		return horizontalCuts[i] < horizontalCuts[j]
	})
	sort.Slice(verticalCuts, func(i, j int) bool {
		return verticalCuts[i] < verticalCuts[j]
	})


	maxHeight := horizontalCuts[0]
	maxWeight := verticalCuts[0]
	for i := 1; i < len(horizontalCuts); i++ {
		maxHeight = max(maxHeight, horizontalCuts[i] - horizontalCuts[i - 1])
	}
	for i := 1; i < len(verticalCuts); i++ {
		maxWeight = max(maxWeight, verticalCuts[i] - verticalCuts[i - 1])
	}

	return maxHeight * maxWeight % MODULO
}
