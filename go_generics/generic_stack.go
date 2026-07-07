/*
implement a stack: an abstract data type which stores items in a last-in-first-out way. The only thing you can do with a stack is “push” a new item onto it, or “pop” the top item off it.

You’ll be building a generic Stack[E] type that holds an ordered collection of values of as broad a range of types as possible.

You’ll need to write a Push method that can append any number of items to the stack, in order, and a Pop method that retrieves (and removes) the last item from the stack.

Pop should also return a second ok value indicating whether an item was actually popped. If the stack is empty, then Pop should return false for this second value, but true otherwise.

Also, you should provide a Len method that returns the number of items in the stack.

For example:

s := Stack[int]{}
fmt.Println(s.Pop())
// 0 false
s.Push(5, 6)
fmt.Println(s.Len())
// 2
v, ok := s.Pop()
fmt.Println(v)
// 6
fmt.Println(ok)
// true
*/
package main

import (
	"fmt"
)

type GenericStack[E any] struct {
	data []E
}

func (s *GenericStack[E]) Push(items ...E) {
	s.data = append(s.data, items...)
}

func (s *GenericStack[E]) Pop() (v E, ok bool) {
	if len(s.data) == 0 {
		return v, ok
	}
	v = s.data[len(s.data)-1]
	s.data = s.data[:len(s.data)-1]
	ok = true
	return
}

func (s *GenericStack[E]) Len() int {
	return len(s.data)
}

func main() {
	s := GenericStack[int]{}
	s.Push(5, 6)
	s.Push(1, 2)
	fmt.Println(s, s.Len())
	val, ok := s.Pop()
	fmt.Println(val, ok)
	fmt.Println(s, s.Len())
	val, ok = s.Pop()
	val, ok = s.Pop()
	val, ok = s.Pop()
	val, ok = s.Pop()
	fmt.Println(val, ok)

	s1 := GenericStack[string]{}
	s1.Push("a", "b", "c")
	fmt.Println(s1.Pop())
}
