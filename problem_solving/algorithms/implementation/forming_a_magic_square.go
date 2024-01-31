package implementation

import (
	"fmt"
)

// func formingMagicSquare(s [][]int32) int32 {
// 	// Write your code here

// }

func main() {

	square := [][]int32{
		[]int32{5, 3, 4},
		[]int32{1, 5, 8},
		[]int32{6, 4, 2},
	}

	square2 := [][]int32{
		[]int32{4, 9, 2},
		[]int32{3, 5, 7},
		[]int32{8, 1, 5},
	}

	var lineSums []int32

	for _, line := range square {
		var lineSum int32 = 0
		for _, item := range line {
			lineSum = lineSum + item
		}
		lineSums = append(lineSums, lineSum)
	}

	var columnSums []int32

	for _, columnIndex := range []int32{0, 1, 2} {
		var columnSum int32 = 0
		for _, line := range square {
			columnSum = columnSum + line[columnIndex]
		}
		columnSums = append(columnSums, columnSum)
	}

	var diagonalSums []int32

	fmt.Println(square)
	fmt.Println(lineSums)
	fmt.Println(columnSums)
}
