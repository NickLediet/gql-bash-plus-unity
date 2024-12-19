#!/bin/bash
source "${LIB_DIR}/response.cgi"
source "${LIB_DIR}/http.cgi"

function bootstrap_server {
  __log "Creating the response...."
  response_create 

  __log "Writing the response..."
  http_header "Status" 200
  http_header "Content-Type" "text/plain"
  http_body "Hello World!"
}
export -f bootstrap_server

 
