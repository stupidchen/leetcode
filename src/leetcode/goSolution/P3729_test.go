package goSolution

import "testing"

func TestScheduleCourse(t *testing.T) {
	courses := [][]int {{100,200},{200,1300},{1000,1250},{2000,3200}}
	AssertEqual(t, 3, scheduleCourse(courses))

	courses = [][]int {{1, 2}, {1, 2}, {2, 4}}
	AssertEqual(t, 3, scheduleCourse(courses))


	courses = [][]int {{3, 2}, {4, 3}}
	AssertEqual(t, 0, scheduleCourse(courses))
}
