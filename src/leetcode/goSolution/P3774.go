package goSolution

type MyCalendar struct {
	events [][]int
}


func MyCalenderConstructor() MyCalendar {
	return MyCalendar{events: make([][]int, 0)}
}


func (this *MyCalendar) Book(start int, end int) bool {
	for _, event := range this.events {
		x, y := event[0], event[1]
		if (start <= x && x < end) || (start < y && y <= end) || (start <= x && y <= end) || (x <= start && end <= y) {
			return false
		}
	}

	this.events = append(this.events, []int{start, end})
	return true
}


/**
 * Your MyCalendar object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */
