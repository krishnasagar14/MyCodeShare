package main

import (
	"fmt"
)

// Consider some data structure for map and reduce problem
type PartAvailability struct {
	PartNumber   string
	UnitCost     float64
	ShippingTax  float64
	PartQuantity int16
	TotalCost    float64
	SupplierName string
}

// transformFunc: transform func for map functional programming applicable on data
type transformFunc[E any] func(E) E

// mapForPartAvail: generic map on custom structure for some computation of its each element.
func mapForPartAvail[PA ~[]*PartAvailability](pa PA, transFunc transformFunc[*PartAvailability]) PA {
	result := make(PA, len(pa))
	for i := range pa {
		result[i] = transFunc(pa[i])
	}
	return result
}

// reduceFunc: reduce func needed to determine one element of custom struct array/ slice
type reduceFunc[E any] func(current, next E) E

// chooseBestSupplierFromPartAvail: real reduce function to determine best supplier based on some criteria defined by reduceFunc
func chooseBestSupplierFromPartAvail[PA ~[]*PartAvailability](pa PA, initPA *PartAvailability, reduFunc reduceFunc[*PartAvailability]) string {
	current := initPA
	for i := range pa {
		current = reduFunc(current, pa[i])
	}
	return current.SupplierName
}

func main() {
	partAvails := []*PartAvailability{
		{
			PartNumber:   "1",
			UnitCost:     10.9,
			ShippingTax:  5.6,
			PartQuantity: 2,
			SupplierName: "Marcone",
		},
		{
			PartNumber:   "1",
			UnitCost:     11.9,
			ShippingTax:  5.9,
			PartQuantity: 1,
			SupplierName: "Reliable",
		},
		{
			PartNumber:   "1",
			UnitCost:     9.9,
			ShippingTax:  5.6,
			PartQuantity: 1,
			SupplierName: "Sundberg",
		},
	}

	// using map mapForPartAvail computed total cost for each part PartAvailability received from supplier
	totalCostComputed := mapForPartAvail(partAvails, func(pa *PartAvailability) *PartAvailability {
		pa.TotalCost = pa.UnitCost*float64(pa.PartQuantity) + pa.ShippingTax
		return pa
	})

	for _, pa := range totalCostComputed {
		fmt.Println(pa.SupplierName, pa.TotalCost)
	}

	// using reduce func find out best supplier of which total cost is low.
	fmt.Println("Choosen supplier:", chooseBestSupplierFromPartAvail(totalCostComputed, totalCostComputed[0], func(current *PartAvailability, next *PartAvailability) *PartAvailability {
		if current.TotalCost <= next.TotalCost {
			return current
		}
		return next
	}))

}
