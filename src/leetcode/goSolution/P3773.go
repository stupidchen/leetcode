package goSolution

import "container/heap"

func maxResult(nums []int, k int) int {
	n := len(nums)

	v := make([]int, n)
	v[0] = nums[0]
	h := &IntTupleMaxHeap{}
	heap.Init(h)
	heap.Push(h, []int{v[0], 0})
	for c := 1; c < n; c++ {
		for t := h.Top()[1]; t < c - k; t = h.Top()[1] {
			heap.Pop(h)
		}

		t := h.Top()[0]
		v[c] = t + nums[c]
		heap.Push(h, []int{v[c], c})
	}
	return v[n - 1]
}
