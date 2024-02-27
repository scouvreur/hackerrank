package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
	"time"
)

var offset int = 0

/*
 * Complete the 'BurstyRateLimiter' function below.
 *
 * The function accepts following parameters:
 *  1. chan bool requestChan
 *  2. chan int resultChan
 *  3. int batchSize
 *  4. int toAdd
 */

func BurstyRateLimiter(requestChan chan bool, resultChan chan int, batchSize int, toAdd int) {
	// start infinite loop
	for {
		// receive the request
		request := <-requestChan

		// rate limit 10 ms
		time.Sleep(10 * time.Millisecond)

		if request {
			// start at offset and send number to
			// result channel
			for i := offset; i < offset+batchSize; i++ {
				resultChan <- i * toAdd
			}

			// increment offset
			offset += batchSize
		}
	}
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	skipTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	skipBatches := int(skipTemp)

	totalTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	printBatches := int(totalTemp)

	batchSizeTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	batchSize := int(batchSizeTemp)

	toAddTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	toAdd := int(toAddTemp)

	resultChan := make(chan int)
	requestChan := make(chan bool)
	go BurstyRateLimiter(requestChan, resultChan, batchSize, toAdd)
	for i := 0; i < skipBatches+printBatches; i++ {
		start := time.Now().UnixNano()
		requestChan <- true
		for j := 0; j < batchSize; j++ {
			new := <-resultChan
			if i < skipBatches {
				continue
			}
			fmt.Println(new)
		}
		if i >= skipBatches && i != skipBatches+printBatches-1 {
			fmt.Println("-----")
		}
		end := time.Now().UnixNano()
		timeDiff := (end - start) / 1000000
		if timeDiff < 3 {
			fmt.Println("Rate is too high")
			break
		}
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
