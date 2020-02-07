package leetcode

type WordDictionary struct {
	t []*WordDictionary
	e bool
	p bool
}


/** Initialize your data structure here. */
func Constructor() WordDictionary {
	var dic = WordDictionary{t: make([]*WordDictionary, 26), e: false, p: false}
	return dic
}


/** Inserts a word into the dict. */
func (this *WordDictionary) AddWord(word string)  {
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
	this.t[c].AddWord(word[1:])
}


/** Returns if the word is in the dict. */
func (this *WordDictionary) Search(word string) bool {
	if len(word) == 0 {
		return this.e
	}
	if word[0] != '.' {
		c := word[0] - 'a'
		if this.t[c] != nil {
			return this.t[c].Search(word[1:])
		}
		return false
	} else {
		ret := false
		for i := 0; i < 26; i++ {
			if this.t[i] != nil {
				ret = ret || this.t[i].Search(word[1:])
			}
			if ret {
				return ret
			}
		}
		return ret
	}
}
