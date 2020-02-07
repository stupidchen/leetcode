package leetcode

func reverseList(head *ListNode) *ListNode {
	var tmp *ListNode = nil
	var last *ListNode = nil
	for i := head; i != nil; i = tmp {
		tmp = i.Next
		i.Next = last
		last = i
	}

	return last
}
