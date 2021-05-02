package goSolution

import (
	"container/heap"
	"sort"
)

func scheduleCourse(courses [][]int) int {
	sort.Slice(courses, func(i, j int) bool {
		return courses[i][1] < courses[j][1]
	})

	h := &IntMaxHeap{}
	heap.Init(h)

	time := 0
	for _, course := range courses {
		duration, lastDay := course[0], course[1]
		time += duration
		heap.Push(h, duration)
		if time > lastDay {
			maxDuration := heap.Pop(h)
			time -= maxDuration.(int)
		}
	}

	return h.Len()
}