package main

import (
	"fmt"
	"sort"
)

// Função de busca binária
func binarySearch(arr []int, target int) int {
	left := 0
	right := len(arr) - 1

	for left <= right {
		mid := (left + right) / 2

		if arr[mid] == target {
			return mid // Retorna o índice do elemento encontrado
		} else if arr[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return -1 // Retorna -1 se o elemento não for encontrado
}

func main() {
	arr := []int{1, 3, 5, 6, 7, 8, 9, 0, 6, 3, 4}

	// Ordenando o array antes da busca binária
	sort.Ints(arr)

	target := 5
	index := binarySearch(arr, target)

	if index != -1 {
		fmt.Printf("Elemento %d encontrado no índice %d\n", target, index)
	} else {
		fmt.Printf("Elemento %d não encontrado\n", target)
	}
}
