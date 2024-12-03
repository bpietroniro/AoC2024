package util

import "fmt"

func GetFilePath(day, filename string) string {
	return fmt.Sprintf("../../puzzles/%s/%s", day, filename)
}
