package goSolution

type WordFilterNode struct {
	child map[int]*WordFilterNode
	val int
}

type WordFilter struct {
	root *WordFilterNode
}

func convertCharacter(str string, index int) int {
	if index >= len(str) {
		return 0
	}

	c := str[index]
	if c == ' ' {
		return 0
	}
	return int(c) - 96
}

func NewWordFilterNode() *WordFilterNode{
	child := make(map[int]*WordFilterNode)

	return &WordFilterNode{child, -1}
}

func (this *WordFilter) AddWord(length int, prefix string, pIndex int, suffix string, sIndex int, node *WordFilterNode, val int) {
	if pIndex > length && sIndex > length {
		node.val = max(node.val, val)
		return
	}

	p, s := convertCharacter(prefix, pIndex), convertCharacter(suffix, sIndex)
	t := p * 10 + s
	if node.child[t] == nil {
		node.child[t] = NewWordFilterNode()
	}
	this.AddWord(length, prefix, pIndex + 1, suffix, sIndex + 1, node.child[t], val)
}

func (this *WordFilter) GetWord(length int, prefix string, pIndex int, suffix string, sIndex int, node *WordFilterNode) int {
	if pIndex > length && sIndex > length {
		return node.val
	}

	p, s := convertCharacter(prefix, pIndex), convertCharacter(suffix, sIndex)
	t := p * 10 + s
	if node.child[t] == nil {
		return -1
	}
	return this.GetWord(length, prefix, pIndex + 1, suffix, sIndex + 1, node.child[t])
}

func Constructor(words []string) WordFilter {
	root := NewWordFilterNode()
	wf := WordFilter{root}

	for index, word := range words {
		n := len(word)
		for pl := 0; pl <= n; pl++ {
			for sl := 0; sl <= n; sl++ {
				wf.AddWord(max(pl, sl), word[:pl], 0, word[n - sl:], 0, root, index)
			}
		}
	}

	return wf
}


func (this *WordFilter) F(prefix string, suffix string) int {
	return this.GetWord(max(len(prefix), len(suffix)), prefix, 0, suffix, 0, this.root)
}
