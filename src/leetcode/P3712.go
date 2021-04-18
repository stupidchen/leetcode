package leetcode

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func countLengthOfList(head *ListNode) int {
	ret := 0
	for ; head != nil; head=head.Next{
		ret += 1
	}
	return ret
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	lengthOfList := countLengthOfList(head)
	n = lengthOfList - n
	pivot := &ListNode{Next: head}
	last := pivot
	node := head
	for i := 0; i < n; i++ {
		last = last.Next
		node = node.Next
	}
	last.Next = node.Next
	return pivot.Next
}
