package goSolution

import "strings"

func findDuplicate(paths []string) [][]string {
	contents := make(map[string][]string)

	for _, path := range paths {
		seg := strings.Split(path, " ")

		dir := seg[0]
		for _, file := range seg[1:] {
			p := strings.Index(file, "(")
			path, content := file[:p], file[p:len(file)-1]
			path = dir + "/" + path

			if contents[content] == nil {
				contents[content] = []string{path}
			} else {
				contents[content] = append(contents[content], path)
			}
		}
	}

	ret := make([][]string, 0)
	for _, values := range contents {
		if len(values) > 1 {
			ret = append(ret, values)
		}
	}
	return ret
}
