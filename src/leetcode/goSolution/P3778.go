package goSolution

import "sort"

func maximumUnits(boxTypes [][]int, truckSize int) int {
	boxTypesTupleArray := IntTupleMaxHeap{}
	for _, boxType := range boxTypes {
		boxTypesTupleArray = append(boxTypesTupleArray, []int{boxType[1], boxType[0]})
	}

	sort.Sort(boxTypesTupleArray)
	ret := 0
	for _, boxType := range boxTypesTupleArray {
		if truckSize >= boxType[1] {
			ret += boxType[1] * boxType[0]
			truckSize -= boxType[1]
		} else {
			ret += min(boxType[1], truckSize) * boxType[0]
			break
		}
	}
	return ret
}
