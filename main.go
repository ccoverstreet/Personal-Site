package main

import (
	"fmt"
	"net/http"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"

	"github.com/ccoverstreet/cale-site/frontend"
)

func main() {
	router := chi.NewRouter()
	router.Use(middleware.Logger)
	compressor := middleware.NewCompressor(5)
	router.Use(compressor.Handler)

	router.Get("/", func(w http.ResponseWriter, r *http.Request) {
		b, err := frontend.IndexFile()
		if err != nil {
			fmt.Fprintf(w, "Site not available")
		}

		w.Header().Set("Content-Type", "text/html")
		w.Write(b)
	})

	fs := http.FileServer(http.Dir("frontend/build"))
	router.Handle("/*", fs)

	http.ListenAndServe(":3333", router)
	fmt.Println("vim-go")
}
