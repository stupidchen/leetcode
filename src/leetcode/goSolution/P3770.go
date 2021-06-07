package goSolution

func minCostClimbingStairs(cost []int) int {
	cost0 := cost[0]
	cost1 := cost[1]
	for _, c := range cost[2:] {
		t := cost1
		cost1 = c + min(t, cost0)
		cost0 = t
	}
	return min(cost1, cost0)
}
