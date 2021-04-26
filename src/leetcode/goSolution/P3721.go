package goSolution

import "sort"

type BuildingDiff struct {
	Diff, Index int
}

type BuildingDiffs []BuildingDiff

func (a BuildingDiffs) Len() int {return len(a)}
func (a BuildingDiffs) Less(i, j int) bool {return a[i].Diff > a[j].Diff || (a[i].Diff == a[j].Diff && a[i].Index < a[j].Index)}
func (a BuildingDiffs) Swap(i, j int) {a[i], a[j] = a[j], a[i]}

func (a BuildingDiffs) CanReachTarget(target int, bricks int, ladders int) bool {
	m := len(a)
	for i := 0; i < m; i++ {
		if a[i].Index <= target {
			if ladders > 0 {
				ladders--
			} else {
				if bricks >= a[i].Diff {
					bricks -= a[i].Diff
				} else {
					return false
				}
			}
		}
	}
	return true
}

func furthestBuilding(heights []int, bricks int, ladders int) int {
	n := len(heights)
	a := BuildingDiffs{}
	for i := 1; i < n; i++ {
		d := heights[i] - heights[i - 1]
		if d > 0 {
			a = append(a, BuildingDiff{Index: i, Diff: d})
		}
	}

	sort.Sort(a)
	ret := 0
	for l, r := 0, n - 1; l <= r; {
		mid := (l + r) >> 1
		if a.CanReachTarget(mid, bricks, ladders) {
			l = mid + 1
			ret = mid
		} else {
			r = mid - 1
		}
	}
	return ret
}
