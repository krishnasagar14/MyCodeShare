package main

import (
	"bufio"
	"fmt"
	"iter"
	"log"
	"os"
	"flag"
)

// problem: there is large file >1GB need memory efficient solution to read the file contents line by line only.

// FileReader: reads any format large files using iterator with low memory profile
func FileReader(filePath string) (iter.Seq2[[]byte, error]) {

	// iterator for reading file line by line with min memory footprint.
	fileIterator := func(yield func([]byte, error) bool) {
		fileObj, err := os.Open(filePath)
		if err != nil {
			yield(nil, err)
			return
		}
		defer fileObj.Close()

		// buffer file IO Reader with setting buffer maxCapacity of MaxInt64 value
		reader := bufio.NewReader(fileObj) // use NewScanner for text files
		buf := make([]byte, 8096)

		// loop on scanner scan to read file from offset
		for {
			nnumBytesRead, err := reader.Read(buf) // memory usage optimized with buffer
			if err != nil {
				yield(nil, err)
				return
			}
			chunk := buf[:nnumBytesRead]
			fmt.Println(string(chunk)) // any processing on data chunk can be attached
			if !yield(chunk, err) {
				return
			}
		}
	}
	return fileIterator
}

func main() {
	filePath := flag.String("file", "", "Path to file to process (required)")

	for data, err := range FileReader(*filePath) {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(string(data))
	}
}
