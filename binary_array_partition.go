package main

import (
	"fmt"
	"slices"
)

// Problem statement: https://interviewing.io/questions/binary-array-partition

func main() {
	Z := []int{1, 0, 1, 0, 1}

	//Z := []int{1, 1, 0, 1, 1}

	//Z := []int{0, 0, 0, 0}

	numOfOnes := 0
	for _, i := range Z {
		if i == 1 {
			numOfOnes += 1
		}
	}

	if numOfOnes == 0 {
		fmt.Println([]int{0, len(Z) - 1})
		return
	}
	if numOfOnes%3 != 0 {
		fmt.Println([]int{-1, -1})
		return
	}

	totalOnes := numOfOnes / 3
	ones := 0
	start0 := slices.Index(Z, 1)
	i := start0

	fmt.Println(totalOnes)

	for ones < totalOnes {
		if Z[i] == 1 {
			ones += 1
		}
		i += 1
	}

	fmt.Println(i, start0)

	l := i - start0
	start1 := slices.Index(Z[start0+l:], 1) + start0 + l
	start2 := slices.Index(Z[start1+l:], 1) + start1 + l

	fmt.Println(start1, start2)

	l = len(Z) - start2

	if slices.Equal(Z[start0:(start0+l)], Z[start1:(start1+l)]) && slices.Equal(Z[start1:(start1+l)], Z[start2:(start2+l)]) {
		fmt.Println([]int{start0 + l - 1, start1 + l})
		return
	} else {
		fmt.Println([]int{-1, -1})
		return
	}

}
