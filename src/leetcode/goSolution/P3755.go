package goSolution

import (
	"strconv"
)

func evalRPN(tokens []string) int {
	stack := make([]int, 0)
	for _, token := range tokens {
		val, err := strconv.ParseInt(token, 10, 64)
		if err == nil {
			stack = append(stack, int(val))
		} else {
			top := len(stack)
			op1, op2 := stack[top - 2], stack[top - 1]
			r := 0
			switch token {
				case "+": {
					r = op1 + op2
					break
				}
				case "-": {
					r = op1 - op2
					break
				}
				case "*": {
					r = op1 * op2
					break
				}
				case "/": {
					r = op1 / op2
					break
				}
			}
			stack = append(stack[:top-2], r)
		}
	}
	return stack[0]
}
