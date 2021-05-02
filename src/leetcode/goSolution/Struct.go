package goSolution

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
    Val int
    Next *ListNode
}

/**
 * Definition for a tree node.
 */
type Node struct {
    Val int
    Children []*Node
}

type FenwickTree struct {
    Val []int
    Len int
}

func LastBit(x int) int {
    return x ^ (x & (x - 1))
}

func NewFenwickTree(length int) *FenwickTree {
    return &FenwickTree{Val: make([]int, length), Len: length}
}

func (this *FenwickTree) update(x int, f func (d int) int) {
    if x == 0 {
        return
    }

    a, n := this.Val, this.Len
    for t := x; t < n; t += LastBit(t) {
        a[t] = f(a[t])
    }
}

func (this *FenwickTree) get(x int, f func (v, d int) int) int {
    r := 0
    a := this.Val
    for t := x; t > 0; t -= LastBit(t) {
        r = f(r, a[t])
    }
    return r
}
type IntMaxHeap []int

func (h IntMaxHeap) Len() int { return len(h) }
func (h IntMaxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h IntMaxHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *IntMaxHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}

func (h *IntMaxHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[0: n - 1]
    return x
}
