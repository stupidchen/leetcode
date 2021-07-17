package goSolution

func threeEqualParts(arr []int) []int {
	count := 0
	n := len(arr)
	for _, num := range arr {
		count += num
	}
	if count % 3 != 0 {
		return []int {-1, -1}
	}
	if count == 0 {
		return []int {0, n - 1}
	}

	trailingZero := 0
	for i := n - 1; i >= 0; i-- {
		if arr[i] == 0 {
			trailingZero += 1
		} else {
			break
		}
	}

	currentNum := 0
	currentOne := 0
	oneInPart := count / 3
	lastNum := -1
	ret := make([]int, 0)
	for i := 0; i < n; i++ {
		if arr[i] == 1 {
			currentOne += 1
		}
		currentNum = ((currentNum << 1) + arr[i]) % MODULO
		if currentOne == oneInPart {
			currentTailingZero := 0
			i += 1
			for ; i < n && currentTailingZero < trailingZero; i++ {
				if arr[i] == 0 {
					currentTailingZero++
				} else {
					return []int {-1, -1}
				}
			}
			if (lastNum != -1) && (lastNum != currentNum) {
				return []int {-1, -1}
			}
			lastNum = currentNum
			currentOne = 0
			currentNum = 0
			i -= 1
			ret = append(ret, i)
		}
	}
	ret = ret[:2]
	ret[1] += 1
	return ret
}
