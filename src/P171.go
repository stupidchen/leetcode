func titleToNumber(s string) int {
    var ret = 0
    if len(s) == 0 {
        return ret
    }

    ret = int(s[0]) - 65
    for i := 1; i < len(s); i += 1 {
        ret = (ret + 1) * 26 + int(s[i]) - 65
    }

    return ret + 1
}
