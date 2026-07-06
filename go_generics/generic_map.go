package main

import (
	"fmt"
	"maps"
	"strings"
)

// transformFunc: transform func for map functional programming applicable on data
type transformFunc[E any] func(E) E

// MapOnSlice: map generic func for map operation on slice
func MapOnSlice[S ~[]E, E any](s S, f transformFunc[E]) S {
	result := make(S, len(s))
	for i := range s {
		result[i] = f(s[i])
	}
	return result
}

// MapOnDictOptions: options for transforming key or value of map
type MapOnDictOptions struct {
	TransformValue, TransformKey, TransformBoth bool
}

// MapOnDict: map generic func operation on its key or value
func MapOnDict[M ~map[K]V, K comparable, V any](m M, fK transformFunc[K], fV transformFunc[V], options *MapOnDictOptions) M {
	result := make(M, len(m))
	for k, v := range maps.All(m) {
		if options.TransformValue {
			result[k] = fV(v)
		} else if options.TransformKey {
			result[fK(k)] = v
		} else if options.TransformBoth {
			result[fK(k)] = fV(v)
		}
	}
	return result
}

func main() {
	s := []string{"a", "b", "c"}
	fmt.Println(MapOnSlice(s, strings.ToUpper))

	s1 := []int{1, 2, 3, 4}
	fmt.Println(MapOnSlice(s1, func(ele int) int {
		return ele * 2
	}))

	m1 := map[string]string{
		"a": "a",
		"b": "b",
	}
	fmt.Println(MapOnDict(m1, strings.ToUpper, strings.ToUpper, &MapOnDictOptions{
		TransformBoth: true,
	}))

	m2 := map[int]string{
		1: "One",
		2: "Two",
	}
	fmt.Println(MapOnDict(m2, func(ele int) int {
		return ele % 10
	}, strings.ToUpper, &MapOnDictOptions{
		TransformBoth: true,
	}))

}
