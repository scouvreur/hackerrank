package implementation

import (
	"fmt"
	"math"
	"strings"
)

/*
 * Complete the 'encryption' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

func encryption(s string) string {
	// Write your code here
	// test := "if man was meant to stay on the ground god would have given us roots"
	s = strings.ReplaceAll(s, " ", "")

	sqrtL := math.Sqrt(float64(len(s)))

	rows := int(math.Floor(sqrtL))
	columns := int(math.Ceil(sqrtL))

	if rows*columns < len(s) {
		rows = columns
	}

	textArray := make([]string, rows)

	for index, _ := range textArray {
		if index == len(textArray)-1 {
			textArray[index] = s[index*columns:]
		} else {
			textArray[index] = s[index*columns : (index+1)*columns]
		}
	}

	fmt.Println(textArray)

	var builder strings.Builder

	for column := 0; column < columns; column++ {
		for _, line := range textArray {
			if column < len(line) {
				builder.WriteString(string(line[column]))
			}
		}
		builder.WriteString(" ")
	}

	encrypted := builder.String()

	return encrypted
}
