package goSolution

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	p := &ListNode{Next: head}
	index := 0
	var last, next *ListNode
	var leftNode, rightNode *ListNode
	var leftInnerNode, rightInnerNode *ListNode
	for c := p; c != nil; c, index = next, index + 1 {
		next = c.Next
		if index >= left && index <= right {
			c.Next = last
			if index == left {
				leftInnerNode = c
			} else {
				if index == right {
					rightInnerNode = c
				}
			}
		} else {
			if index == left-1 {
				leftNode = c

			} else {
				if index == right+1 {
					rightNode = c
				}
			}
		}
		last = c
	}

	if leftNode != nil && rightInnerNode != nil {
		leftNode.Next = rightInnerNode
	}
	if leftInnerNode != nil {
		leftInnerNode.Next = rightNode
	}
	return p.Next
}
