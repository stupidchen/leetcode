func insertionSortList(head *ListNode) *ListNode {
	var new_head = &ListNode{
		Next: nil,
		Val: int(0x7FFFFFFF + 1),
	}

	var tmp *ListNode
	for i := head; i != nil; i = tmp {
		tmp = i.Next
		var tmp2 *ListNode
		for j := new_head; j != nil; j = tmp2 {
			tmp2 = j.Next
			if j.Next == nil || j.Next.Val > i.Val {
				var next = j.Next
				j.Next = i
				i.Next = next
				break
			}
		}
	}

	return new_head.Next
}