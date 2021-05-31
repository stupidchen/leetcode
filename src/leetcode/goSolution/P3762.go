package goSolution

import "sort"

func suggestedProducts(products []string, searchWord string) [][]string {
	sortedProducts := sort.StringSlice{}
	for _, product := range products {
		sortedProducts = append(sortedProducts, product)
	}

	sort.Sort(sortedProducts)
	n := len(products)
	ret := make([][]string, 0)
	for i := 1; i <= len(searchWord); i++ {
		t := searchWord[:i]
		j := sort.SearchStrings(sortedProducts, t)
		for ; j < n && len(sortedProducts[j]) < i; j++ {
		}

		matchedProducts := make([]string, 0)
		for ; j < n && len(matchedProducts) < 3 && (len(sortedProducts[j]) >= i && sortedProducts[j][:i] == t); j++ {
			matchedProducts = append(matchedProducts, sortedProducts[j])
		}
		ret = append(ret, matchedProducts)
	}
	return ret
}
