package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
	"time"
)

func timer(name string) func() {
	start := time.Now()
	return func() {
		fmt.Printf("%s took %v\n", name, time.Since(start))
	}
}

func main() {
	defer timer("main")()

	f, err := os.Open("day1.test")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	buf := make([]byte, 64*1024)
	scanner.Buffer(buf, bufio.MaxScanTokenSize)

	const estimatedLines = 1000
	left := make([]int, 0, estimatedLines)
	right := make([]int, 0, estimatedLines)

	for scanner.Scan() {
		parts := strings.Fields(scanner.Text())
		if len(parts) != 2 {
			fmt.Println("Row has more than 2 values")
			return
		}

		var1, err1 := strconv.Atoi(parts[0])
		var2, err2 := strconv.Atoi(parts[1])
		if err1 != nil || err2 != nil {
			fmt.Println("Error converting values to integers")
			return
		}

		left = append(left, var1)
		right = append(right, var2)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	sum := part1(left, right)
	fmt.Println(sum)
}

func part1(left, right []int) int {
	sort.Ints(left)
	sort.Ints(right)

	sum := 0
	for i := 0; i < len(left); i++ {
		diff := left[i] - right[i]
		if diff < 0 {
			diff = -diff
		}

		sum += diff
	}

	return sum
}
