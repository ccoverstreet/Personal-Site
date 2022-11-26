package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"

	"github.com/ccoverstreet/calesite/backend/global"
	"github.com/gorilla/mux"
	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
)

func createRouter() *mux.Router {
	router := mux.NewRouter()
	router.HandleFunc("/", RootHandler) // Routes to /home
	router.HandleFunc("/assets/{file}", AssetsHandler)
	router.HandleFunc("/{page}", PageHandler)

	return router
}

func httpErrorHandler(w http.ResponseWriter, r *http.Request, err error) {
	log.Error().
		Err(err).
		Str("request", r.URL.RawPath).
		Msg("Error handling Request")
	log.Printf("Error handling request \"%s\"", r.URL)
}

func RootHandler(w http.ResponseWriter, r *http.Request) {
	http.Redirect(w, r, "/home", 301)
}

var AssetsMap = map[string]string{ // Maps to MIME type
	"standard.css":     "text/css",
	"home.css":         "text/css",
	"Portrait.jpg":     "image/jpeg",
	"material.min.css": "text/css",
}

func AssetsHandler(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	mime, ok := AssetsMap[vars["file"]]
	if !ok {
		httpErrorHandler(w, r, fmt.Errorf("Invalid asset requested."))
		return
	}

	file, err := ioutil.ReadFile(global.WEBROOT + "/" + vars["file"])
	if err != nil {
		httpErrorHandler(w, r, err)
		return
	}

	log.Printf("%v", mime)
	w.Header().Set("Content-Type", "text/css")
	fmt.Fprintf(w, "%s", file)
}

type Page struct {
	RouteHandle func(http.ResponseWriter, *http.Request)
}

var PageTable = map[string]Page{
	"home": Page{HomeRouteHandle},
}

func PageHandler(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	log.Printf("%v", vars)
	page := vars["page"]
	if _, ok := PageTable[page]; !ok {
		httpErrorHandler(w, r, fmt.Errorf("Page does not exist"))
		return
	}

	file, err := ioutil.ReadFile(global.WEBROOT + "/" + page + ".html")
	if err != nil {
		httpErrorHandler(w, r, err)
		return
	}

	w.WriteHeader(http.StatusOK)
	fmt.Fprintf(w, "%s", file)
}

func HomeRouteHandle(w http.ResponseWriter, r *http.Request) {

}

func main() {
	log.Logger = log.Output(zerolog.ConsoleWriter{Out: os.Stderr}).With().Caller().Logger()
	router := createRouter()
	log.Info().Msg("Starting personal website...")
	http.ListenAndServe(":8080", router)
}
