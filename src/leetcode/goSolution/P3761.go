package goSolution

import "math"

func maximumGap(nums []int) int {
	n := len(nums)
	if n < 2 {
		return 0
	}

	minNum, maxNum := min(nums...), max(nums...)
	if minNum == maxNum {
		return 0
	}
	m := (maxNum - minNum - 1) / (n - 1) + 1
	bucket := make([][]int, n)
	for i := 0; i < n; i++ {
		bucket[i] = []int{math.MaxInt64, math.MinInt64}
	}

	for _, num := range nums {
		bucketIndex := (num - minNum) / m
		bucket[bucketIndex][0] = min(bucket[bucketIndex][0], num)
		bucket[bucketIndex][1] = max(bucket[bucketIndex][1], num)
	}

	ret := 0
	last := -1
	for i := 0; i < n; i++ {
		if bucket[i][0] == math.MaxInt64 {
			continue
		}
		if last != -1 {
			ret = max(ret, bucket[i][0] - last)
		}
		last = bucket[i][1]
	}
	return ret
}
