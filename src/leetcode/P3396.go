func removeElements(head *ListNode, val int) *ListNode {
	var first = ListNode{
		Next:head,
	}

	var last = &first
	for tmp := head; tmp != nil; tmp = tmp.Next {
		if tmp.Val == val {
			last.Next = tmp.Next
		} else {
			last = tmp
		}
	}

	return first.Next
}