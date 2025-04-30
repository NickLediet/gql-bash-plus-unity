#!/usr/bin/bash
source "${LIB_DIR}/http.cgi"
source "${LIB_DIR}/request.cgi"

get-request-body post_data

log "Writing the response..."
log "Content-Length: $content_length"
log "Post data w/updated syntax: $post_data"
http-header "Status" 200
http-header "Content-Type" "application/json"
http-json-body "--arg \"message\" \"We did it but with $REQUEST_METHOD!\" --argjson post_data '$post_data'"

