func convertToTitle(n int) string {
    if n == 0 {
        return ""
    }

    n -= 1
    return convertToTitle(n / 26) + string(rune(n % 26 + 65))
}
