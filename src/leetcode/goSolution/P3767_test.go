package goSolution

import "testing"

func TestOpenLock(t *testing.T) {
	AssertEqual(t, -1, openLock([]string{"8887","8889","8878","8898","8788","8988","7888","9888"}, "8888"))
}
