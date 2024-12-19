#!/bin/bash
source "${LIB_DIR}/log.cgi"
source "${LIB_DIR}/bootstrap-server.cgi"
source "${LIB_DIR}/response.cgi"

log "Bootrapping the server..."
bootstrap-server

log "============ HTTP RESPONSE ================"
log-file "${TEMP_DIR}/${REQUEST_UUID}"
log "============= COMPLETE ===================="

# Print the request file to stdout, and then remove it
session_file="${TEMP_DIR}/${REQUEST_UUID}"
cat "${session_file}" && rm -rf "${session_file}"
