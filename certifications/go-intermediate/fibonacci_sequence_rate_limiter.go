// FibonacciSequence rate limiter

package main

import (
	"bufio"
	"fmt"
	"io"
	"math"
	"os"
	"strconv"
	"strings"
	"time"
)

var memo = map[int]int{
	0: 0,
	1: 1,
	2: 2,
}
var lastKey int = 0
var modulo int = int(math.Pow(10, 9))

/*
 * Complete the 'ModuloFibonacciSequence' function below.
 *
 * The function accepts following parameters:
 *  1. chan bool requestChan
 *  2. chan int resultChan
 */
func ModuloFibonacciSequence(requestChan chan bool, resultChan chan int) {
	// start an infinite loop listening for requests
	for {
		// receive request
		request := <-requestChan

		if request {
			// rate limit
			time.Sleep(10 * time.Millisecond)

			_, exists := memo[lastKey+1]
			// if key doesn't exist
			if !exists {
				memo[lastKey+1] = (memo[lastKey] + memo[lastKey-1]) % modulo
			}
			result := memo[lastKey+1]

			// increment lastKey
			lastKey++

			// send result to the result channel
			resultChan <- result
		}
	}
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	skipTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	skip := int32(skipTemp)

	totalTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	total := int32(totalTemp)

	resultChan := make(chan int, 10)
	requestChan := make(chan bool, 10)
	go ModuloFibonacciSequence(requestChan, resultChan)
	for i := int32(0); i < skip+total; i++ {
		start := time.Now().UnixNano()
		requestChan <- true
		new := <-resultChan
		if i < skip {
			continue
		}
		end := time.Now().UnixNano()
		timeDiff := (end - start) / 1000000
		if timeDiff < 3 {
			fmt.Println("Rate is too high")
			break
		}
		fmt.Println(new)
	}
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
