package frontend

import (
	"os"
)

func IndexFile() ([]byte, error) {
	return os.ReadFile("frontend/build/index.html")
}
