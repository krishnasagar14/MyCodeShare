package main

import (
	"fmt"
	"strings"
)

// Generic type LRU cache data structure
type GenericLRUCache[K comparable, V any] struct {
	Data     map[K]V
	MaxSize  int16     // max size of cache
	currSize int16     // counter of current cache size
	Counter  map[K]int // Counter will store count value of each cache key
}

// GET func to fetch value of key from cache
func (c *GenericLRUCache[K, V]) Get(key K) (val V) {
	if val, ok := c.Data[key]; ok {
		c.Counter[key] += 1 // assuming key exists always if it exists in Data
		return val
	}
	return val
}

// SET func to store key, value in cache
// Manages cache key invalidation if cache capacity is full
func (c *GenericLRUCache[K, V]) Set(newKey K, newVal V) {
	if c.currSize == c.MaxSize {
		// cache capacity is full; delete least used key
		for key, val := range c.Counter {
			if val == 0 {
				delete(c.Data, key)
				delete(c.Counter, key)
				c.MaxSize -= 1
				break
			}
		}
	} else if _, ok := c.Data[newKey]; ok {
		// if key exists in cache; delete its data and counter metadata
		delete(c.Data, newKey)
		delete(c.Counter, newKey)
		c.MaxSize -= 1
	}
	c.Data[newKey] = newVal
	c.Counter[newKey] = 0
	c.currSize += 1
}

func (c *GenericLRUCache[K, V]) Print() {
	for key, val := range c.Data {
		fmt.Println(key, ":", val)
	}
}

func NewTextLRUCache[K string, V string](size int16) *GenericLRUCache[K, V] {
	return &GenericLRUCache[K, V]{
		Data:    make(map[K]V, size),
		MaxSize: size,
		Counter: make(map[K]int, size),
	}
}

func main() {
	lruCache := NewTextLRUCache(10)
	for ch := 'a'; ch <= 'z'; ch++ {
		alpha := string(ch)
		lruCache.Set(string(alpha), strings.ToUpper(alpha))
	}
	lruCache.Set("z", "Z1")
	fmt.Println("value:", lruCache.Get("abc")) // value:
	lruCache.Print()
	/*
		j : J
		r : R
		a : A
		d : D
		e : E
		k : K
		n : N
		p : P
		s : S
		x : X
		c : C
		f : F
		m : M
		o : O
		q : Q
		u : U
		y : Y
		z : Z1
		b : B
		g : G
		t : T
		v : V
		w : W
		l : L
		i : I
	*/
}
