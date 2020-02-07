package leetcode

type Trie struct {
	t []*Trie
	e bool
	p bool
}


/** Initialize your data structure here. */
func Constructor() Trie {
	var trie = Trie{t: make([]*Trie, 26), e: false, p: false}
	return trie
}


/** Inserts a word into the trie. */
func (this *Trie) Insert(word string)  {
	if len(word) == 0 {
		this.e = true
		return
	}
	c := word[0] - 'a'
	if this.t[c] == nil {
		tmp := Constructor()
		this.t[c] = &tmp
	}
	this.t[c].p = true
	this.t[c].Insert(word[1:])
}


/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
	if len(word) == 0 {
		return this.e
	}
	c := word[0] - 'a'
	if this.t[c] != nil {
		return this.t[c].Search(word[1:])
	}
	return false
}


/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
	if len(prefix) == 0 {
		return this.p
	}
	c := prefix[0] - 'a'
	if this.t[c] != nil {
		return this.t[c].StartsWith(prefix[1:])
	}
	return false
}
