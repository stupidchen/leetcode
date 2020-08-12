func getRow(rowIndex int) []int {
	var f [2][1000000]int
	f[0][0] = 1
	f[1][0] = 1
	f[1][1] = 1
	for i := 2; i <= rowIndex; i++ {
		for j := 0; j <= i; j++ {
			var l = 0
			if j > 0 {
				l = f[1 - (i & 1)][j - 1]
			}
			var r = f[1 - (i & 1)][j]
			f[i & 1][j] = l + r
		}
	}
	return f[rowIndex & 1][0:rowIndex+1]
}

func main() {
	getRow(0)
}