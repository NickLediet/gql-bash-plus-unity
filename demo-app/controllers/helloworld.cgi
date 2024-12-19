#!/bin/bash
source "${LIB_DIR}/http.cgi"

log "Writing the response..."
http-header "Status" 200
http-header "Content-Type" "text/plain"
http-body "Hello World!"

