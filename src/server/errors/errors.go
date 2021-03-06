package errors

import (
	"encoding/json"
	"net/http"
)

// Generates internal server error response.
func CreateInternalServerErrorResponse(rw http.ResponseWriter, err error) {
	rw.WriteHeader(http.StatusInternalServerError)
	json.NewEncoder(rw).Encode(map[string]interface{}{
		"error": err.Error(),
	})
}

// Generates bad request error response.
func CreateBadRequestErrorResponse(rw http.ResponseWriter, err error) {
	rw.WriteHeader(http.StatusBadRequest)
	json.NewEncoder(rw).Encode(map[string]interface{}{
		"error": err.Error(),
	})
}
