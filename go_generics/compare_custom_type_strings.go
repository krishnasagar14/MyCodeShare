package main

import "fmt"

// This constraint accepts string or any type whose underlying type is string
type StringLike interface {
	~string
}

func CompareString[T1, T2 StringLike](ele1 T1, ele2 T2) bool {
	return string(ele1) == string(ele2)
	// return ele1 == ele2
}

type MyCustomString string
type AnotherCustStr string

func main() {
	var normalStr MyCustomString = "hello"
	var customStr AnotherCustStr = "world"

	// Compare two custom types of base string type using generics
	fmt.Println(CompareString(normalStr, customStr))
}
