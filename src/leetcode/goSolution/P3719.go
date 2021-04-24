package goSolution

type BridgeFinder struct {
	time int
	edges [][]int
	nodes int
	tin, low []int
	visited []bool
	bridges [][]int
}

func (bf *BridgeFinder) FindBridge(nodes int, edgeList [][]int) [][]int {
	bf.nodes = nodes
	bf.time = 0
	bf.tin, bf.low = make([]int, nodes), make([]int, nodes)
	bf.visited = make([]bool, nodes)
	bf.bridges = [][]int{}
	bf.edges = make([][]int, nodes)
	for _, edge := range edgeList {
		x, y := edge[0], edge[1]
		bf.edges[x] = append(bf.edges[x], y)
		bf.edges[y] = append(bf.edges[y], x)
	}

	for i := 0; i < nodes; i++ {
		if !bf.visited[i] {
			bf.find(-1, 0)
		}
	}
	return bf.bridges
}

func (bf *BridgeFinder) find(parent int, node int) {
	bf.visited[node] = true
	bf.tin[node], bf.low[node] = bf.time, bf.time
	bf.time++
	for _, child := range bf.edges[node] {
		if child == parent {
			continue
		}
		if bf.visited[child] {
			bf.low[node] = min(bf.tin[child], bf.low[node])
		} else {
			bf.find(node, child)
			bf.low[node] = min(bf.low[child], bf.low[node])
			if bf.low[child] > bf.tin[node] {
				bf.bridges = append(bf.bridges, []int{node, child})
			}
		}
	}
}

func criticalConnections(n int, connections [][]int) [][]int {
	bf := BridgeFinder{}
	return bf.FindBridge(n, connections)
}
