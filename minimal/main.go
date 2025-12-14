package main

import (
	"fmt"
	"net/http"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
)

func main() {
	// Using chi
	router := chi.NewRouter()
	router.Use(middleware.Logger)
	compressor := middleware.NewCompressor(5)
	router.Use(compressor.Handler)

	fs := http.FileServer(http.Dir("./html"))
	router.Handle("/*", fs)

	http.ListenAndServe(":3333", router)
	fmt.Println("vim-go")
}
