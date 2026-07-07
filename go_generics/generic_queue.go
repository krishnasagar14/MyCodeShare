package main

import (
	"fmt"
)

type GenericQueue[E any] struct {
	data []E
}

func (s *GenericQueue[E]) Enqueue(items ...E) {
	s.data = append(s.data, items...)
}

func (s *GenericQueue[E]) Dequeue() (v E, ok bool) {
	if len(s.data) == 0 {
		return v, ok
	}
	v = s.data[0]
	s.data = s.data[1:]
	ok = true
	return
}

func (s *GenericQueue[E]) Len() int {
	return len(s.data)
}

func main() {
	s := GenericQueue[int]{}
	s.Enqueue(5, 6)
	s.Enqueue(1, 2)
	fmt.Println(s, s.Len())
	val, ok := s.Dequeue()
	fmt.Println(val, ok)
	fmt.Println(s, s.Len())
	val, ok = s.Dequeue()
	val, ok = s.Dequeue()
	val, ok = s.Dequeue()
	val, ok = s.Dequeue()
	fmt.Println(val, ok)

	s1 := GenericQueue[string]{}
	s1.Enqueue("a", "b", "c")
	fmt.Println(s1.Dequeue())
}
