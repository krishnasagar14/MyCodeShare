package main

import (
	"fmt"
)

// GenericSet: generic data structure defining set
type GenericSet[E comparable] map[E]struct{}

// NewGenericSet: generic func to create set with items
func NewGenericSet[E comparable](items ...E) GenericSet[E] {
	s := GenericSet[E]{}
	for _, i := range items {
		s[i] = struct{}{}
	}
	return s
}

// Add: generic func to add items into set
func (s GenericSet[E]) Add(items ...E) {
	for _, i := range items {
		s[i] = struct{}{}
	}
}

// Contains: generic func to know if item exist in set
func (s GenericSet[E]) Contains(item E) bool {
	if _, ok := s[item]; ok {
		return true
	}
	return false
}

// Members: generic func fetch all items of set
func (s GenericSet[E]) Members() []E {
	result := make([]E, 0, len(s))
	for i := range s {
		result = append(result, i)
	}
	return result
}

// Union: generic func to find union of sets
func (s GenericSet[E]) Union(s1 GenericSet[E]) []E {
	result := NewGenericSet(s.Members()...)
	result.Add(s1.Members()...)
	return result.Members()
}

// Intersection: generic func to find intersection between sets
func (s GenericSet[E]) Intersection(s1 GenericSet[E]) []E {
	result := make([]E, 0, len(s))
	for i := range s1 {
		if s.Contains(i) {
			result = append(result, i)
		}
	}
	return result
}

func main() {
	s := NewGenericSet(1, 2, 3)
	fmt.Println(s.Contains(0))
	fmt.Println(s.Members())
	s1 := NewGenericSet(1, 2, 3, 5)
	fmt.Println(s.Union(s1))
	fmt.Println(s.Intersection(s1))
	// below will lead to error: cannot use s2 (variable of map type GenericSet[string]) as GenericSet[int] value in argument to s.Union
	// s2 := NewGenericSet("1", "2")
	// fmt.Println(s.Union(s2))

	// GenericSet application in profile matching to job specs problem
	jobSkills := NewGenericSet("go", "java")
	mySkills := NewGenericSet("go", "ruby")
	matches := jobSkills.Intersection(mySkills)
	if len(matches) > 0 {
		fmt.Println("You're hired!")
	}
}
