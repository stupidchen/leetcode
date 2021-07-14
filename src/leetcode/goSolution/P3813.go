package goSolution

import (
	"sort"
)

func customSortString(order string, str string) string {
	orderMap := make(map[rune]int)
	reversedOrderMap := make(map[int]rune)
	for i, char := range order {
		orderMap[char] = i
		reversedOrderMap[i] = char
	}

	i := len(order)
	charList := make([]int, 0)
	for _, char := range str {
		val, ok := orderMap[char]
		if !ok {
			orderMap[char] = i
			reversedOrderMap[i] = char
			val = i
			i++
		}
		charList = append(charList, val)
	}

	sort.Ints(charList)
	ret := ""
	for _, o := range charList {
		ret = ret + string(reversedOrderMap[o])
	}
	return ret
}
