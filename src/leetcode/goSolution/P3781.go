package goSolution

func generateParenthesisRecursively(n int, currentIndex int, currentString string, parValue int, results *[]string) {
	if n == currentIndex {
		*results = append(*results, currentString)
		return
	}

	if n - currentIndex - 1 >= parValue + 1 {
		generateParenthesisRecursively(n, currentIndex + 1, currentString + "(", parValue + 1, results)
	}
	if parValue > 0 {
		generateParenthesisRecursively(n, currentIndex + 1, currentString + ")", parValue - 1, results)
	}

}

func generateParenthesis(n int) []string {
	ret := make([]string, 0)
	generateParenthesisRecursively(n << 1, 0, "", 0, &ret)
	return ret
}
