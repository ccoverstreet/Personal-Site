package global

import (
	"log"
	"os"
	"path"
)

var ROOT string
var WEBROOT string

func init() {
	log.Println("Initializing Globals...")
	exe, err := os.Executable()
	if err != nil {
		log.Println("Unable to retrieve current executable.")
		panic(err)
	}

	ROOT = path.Dir(exe)
	WEBROOT = ROOT + "/html"
}
