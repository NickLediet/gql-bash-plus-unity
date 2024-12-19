#!/bin/bash
source "${LIB_DIR}/response.cgi"
source "${LIB_DIR}/router.cgi"

function bootstrap-server {
  log "Creating the response...."
  response-create
  log "Pass the request to the router to be resolved..."
  router-process
}
export -f bootstrap-server

 
