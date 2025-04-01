#!/usr/bin/bash
source "${LIB_DIR}/http.cgi"

log "Writing the response..."
http-header "Status" 200
http-header "Content-Type" "application/json"
http-json-body "--arg \"message\" \"We did it but with $REQUEST_METHOD!\""

