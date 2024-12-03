package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"sort"
	"strconv"
)

func main() {
	left, right := parseInput("input.txt")
	total := totalDistance(left, right)
	score := similarityScore()

	fmt.Println(total)
	fmt.Println(score)
}

// TODO
func similarityScore() int32 {
	var score int32 = 0

	return score
}

func totalDistance(left, right []int32) int32 {
	sort.Slice(left, func(i, j int) bool { return left[i] < left[j] })
	sort.Slice(right, func(i, j int) bool { return right[i] < right[j] })

	var total int32 = 0
	for i := range left {
		difference := left[i] - right[i]
		if difference >= 0 {
			total += difference
		} else {
			total -= difference
		}
	}

	return total
}

func parseInput(filename string) ([]int32, []int32) {
	file, err := os.Open(fmt.Sprintf("../../puzzles/01/%s", filename))
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var list1, list2 []int32
	re := regexp.MustCompile(`\s+`)

	for scanner.Scan() {
		numbers := re.Split(scanner.Text(), -1)

		num1, err := strconv.ParseInt(numbers[0], 10, 32)
		if err != nil {
			log.Fatal(err)
		}
		num2, err := strconv.ParseUint(numbers[1], 10, 32)
		if err != nil {
			log.Fatal(err)
		}

		list1 = append(list1, int32(num1))
		list2 = append(list2, int32(num2))
	}

	return list1, list2
}
