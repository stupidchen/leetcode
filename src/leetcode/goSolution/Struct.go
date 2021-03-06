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

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
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

func (h *IntMaxHeap) Top() int {
    return (*h)[0]
}

type IntTupleMaxHeap [][]int
func (h IntTupleMaxHeap) Len() int { return len(h) }
func (h IntTupleMaxHeap) Less(i, j int) bool { return h[i][0] > h[j][0] }
func (h IntTupleMaxHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *IntTupleMaxHeap) Push(x interface{}) {
    *h = append(*h, x.([]int))
}

func (h *IntTupleMaxHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[0: n - 1]
    return x
}

func (h *IntTupleMaxHeap) Top() []int {
    return (*h)[0]
}

type DSU struct {
    Set []int
    Rank []int
}

func InitializeDSU(size int) *DSU {
    ret := &DSU {
        Set: make([]int, size),
        Rank: make([]int, size),
    }
    ret.Reset()
    return ret
}
func (d *DSU) Reset() {
    for i := 0; i < d.Len(); i++ {
        d.Set[i] = i
        d.Rank[i] = 1
    }
}
func (d *DSU) Len() int { return len(d.Set) }
func (d *DSU) FindSet(x int) int {
    var t int
    for t = x; d.Set[t] != t; t = d.Set[t] {}
    for ; d.Set[x] != x; {
        d.Set[x], x = t, d.Set[x]
    }
    return t
}
func (d *DSU) MergeSet(x, y int) {
    sx, sy := d.FindSet(x), d.FindSet(y)
    if d.Rank[sx] > d.Rank[sy] {
        d.Set[sy] = d.Set[sx]
    } else {
        d.Set[sx] = d.Set[sy]
        if d.Rank[sx] == d.Rank[sy] {
            d.Rank[sy]++
        }
    }
}
