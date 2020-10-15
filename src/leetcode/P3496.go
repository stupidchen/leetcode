func swap(x *int, y *int) {
	if *x == *y {
		return
	}
	*x = *x ^ *y
	*y = *x ^ *y
	*x = *x ^ *y
}

func reverse(arr []int, l int, r int) {
	for i := 0; r - i > l + i; i++ {
		swap(&arr[l + i], &arr[r - i])
	}
}

func rotate(nums []int, k int)  {
	var n = len(nums)
	k %= n
	if k <= 0 {
		return
	}

	reverse(nums, 0, n - 1)
	reverse(nums, 0, k - 1)
	reverse(nums, k, n - 1)
}
