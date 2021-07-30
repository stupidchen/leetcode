package goSolution

import "strings"

type MapSum struct {
	values map[string]int
}


/** Initialize your data structure here. */
func ConstructorOfMapSum() MapSum {
	return MapSum{values: make(map[string]int)}
}


func (this *MapSum) Insert(key string, val int)  {
	this.values[key] = val
}


func (this *MapSum) Sum(prefix string) int {
	ret := 0
	for key, val := range this.values {
		if strings.HasPrefix(key, prefix) {
			ret += val
		}
	}
	return ret
}
