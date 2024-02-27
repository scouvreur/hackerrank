// Problem statement
// We want to insert and merge if needed an interval
// into a set of existing intervals

// Initial intervals
// <4,7><10,15><20,21>

// Case 0
// No overlap
// To insert
// <16,17>

// Should return
// <4,7><10,15><16,17><20,21>

// Case 1
// Partial overlap case - 1 interval
// To insert
// <5,8>

// Should return
// <4,8><10,15><20,21>

// Case 2
// Partial overlap case - 2+ intervals
// To insert
// <5,14>

// Should return
// <4,15><20,21>

// Case 3
// Multiple overlap case - to the end
// To insert
// <13,30>

// Should return
// <4,7><10,30>

package main

import (
	"fmt"
	"os"
	"reflect"
	"strings"
)

// DEBUG MODE
var debug bool = false

var dashes string = strings.Repeat("-", 60)

func MergeIntoIntervals(initialIntervals [][]int, toInsert []int) [][]int {

	// Create MergePointer type
	type MergePointer struct {
		Index  int
		Locked bool
	}

	// Initialize pointer structs
	start := MergePointer{Index: 0, Locked: false}
	end := MergePointer{Index: 0, Locked: false}

	// Initialize values
	isInsert := false

	for index, interval := range initialIntervals {
		// lowerBound := interval[0]
		upperBound := interval[1]

		// look at current interval
		if upperBound > toInsert[0] && !start.Locked {
			start.Index = index
			start.Locked = true
		}

		// peek at the next interval
		if index+1 <= len(initialIntervals)-1 {
			if initialIntervals[index+1][0] > toInsert[1] && !end.Locked {
				end.Index = index
				end.Locked = true
			}

			// check if it's a pure insert
			if toInsert[0] > upperBound && toInsert[1] < initialIntervals[index+1][0] {
				isInsert = true
			}
		}

		if upperBound > toInsert[1] && !end.Locked {
			end.Index = index
			end.Locked = true
		}
	}

	// DEBUG MODE
	if debug {
		fmt.Printf("start: %+v\n", start)
		fmt.Printf("end: %+v\n", end)
		fmt.Println("isInsert:", isInsert)
	}

	// if start.Index == end.Index && start.Locked && end.Locked {
	if isInsert {
		// Simple insert
		newIntervals := make([][]int, len(initialIntervals)+1)

		for index := range newIntervals {
			if index < start.Index {
				newIntervals[index] = initialIntervals[index]
			} else if index == start.Index {
				newIntervals[index] = toInsert
			} else {
				newIntervals[index] = initialIntervals[index-1]
			}
		}

		return newIntervals

	} else {
		// some merge scenario
		if end.Index == 0 && !end.Locked {
			// Merge scenario - to the end
			// case when we need to merge all the way to the end
			newIntervals := make([][]int, len(initialIntervals[:start.Index])+1)

			for index := range newIntervals {
				if index < start.Index {
					newIntervals[index] = initialIntervals[index]
				} else if index == start.Index {
					newIntervals[index] = []int{0, 0}
					newIntervals[index][0] = min(initialIntervals[index][0], toInsert[0])
					newIntervals[index][1] = max(initialIntervals[index][1], toInsert[1])
				}
			}

			return newIntervals
		} else if start.Index == end.Index && end.Locked {
			// Merge scenario - 1 interval
			initialIntervals[start.Index][0] = min(initialIntervals[start.Index][0], toInsert[0])
			initialIntervals[start.Index][1] = max(initialIntervals[start.Index][1], toInsert[1])

			return initialIntervals
		} else if end.Index > start.Index && end.Locked {
			// Merge scenario - 2+ intervals
			newIntervals := make([][]int, len(initialIntervals)-(end.Index-start.Index))

			for index := range newIntervals {
				if index < start.Index {
					newIntervals[index] = initialIntervals[index]
				} else if index == start.Index {
					newIntervals[index] = []int{0, 0}
					newIntervals[index][0] = min(initialIntervals[index][0], toInsert[0])
					newIntervals[index][1] = max(initialIntervals[end.Index][1], toInsert[1])
				} else {
					newIntervals[index] = initialIntervals[index+end.Index-start.Index]
				}
			}
			return newIntervals
		} else {
			return [][]int{{}}
		}
	}
}

func main() {
	// DEBUG MODE
	if len(os.Args) > 1 && os.Args[1] == "--debug" {
		debug = true
	}

	type TestCase struct {
		description       string
		initialIntervals  [][]int
		toInsert          []int
		expectedIntervals [][]int
	}

	testCases := []TestCase{
		{
			description:       "Test Case 0 - Simple insert",
			initialIntervals:  [][]int{{4, 7}, {10, 15}, {20, 21}},
			toInsert:          []int{16, 17},
			expectedIntervals: [][]int{{4, 7}, {10, 15}, {16, 17}, {20, 21}},
		},
		{
			description:       "Test Case 1 - Merge scenario - 1 interval",
			initialIntervals:  [][]int{{4, 7}, {10, 15}, {20, 21}},
			toInsert:          []int{5, 8},
			expectedIntervals: [][]int{{4, 8}, {10, 15}, {20, 21}},
		},
		{
			description:       "Test Case 2 - Merge scenario - 2+ intervals",
			initialIntervals:  [][]int{{4, 7}, {10, 15}, {20, 21}},
			toInsert:          []int{5, 14},
			expectedIntervals: [][]int{{4, 15}, {20, 21}},
		},
		{
			description:       "Test Case 3 - Merge scenario - to the end",
			initialIntervals:  [][]int{{4, 7}, {10, 15}, {20, 21}},
			toInsert:          []int{13, 30},
			expectedIntervals: [][]int{{4, 7}, {10, 30}},
		},
	}

	for index, testCase := range testCases {
		fmt.Println(dashes)

		// Print test case data
		fmt.Println(testCase.description)
		fmt.Println("Initial intervals:", testCase.initialIntervals)
		fmt.Println("To insert:", testCase.toInsert)

		got := MergeIntoIntervals(testCase.initialIntervals, testCase.toInsert)

		fmt.Println("Got intervals:", got)
		fmt.Println("Expected intervals:", testCase.expectedIntervals)

		match := reflect.DeepEqual(got, testCase.expectedIntervals)

		fmt.Println("Match:", match)

		if index == len(testCases)-1 {
			fmt.Println(dashes)
		}
	}
}
