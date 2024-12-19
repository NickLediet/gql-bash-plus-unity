#!/bin/bash
source "${LIB_DIR}/log.cgi"
source "${LIB_DIR}/bootstrap_server.cgi"
source "${LIB_DIR}/response.cgi"

__log "Bootrapping the server..."
bootstrap_server

__log "============ HTTP RESPONSE ================"
__log_file "${TEMP_DIR}/${REQUEST_UUID}"
__log "============= COMPLETE ===================="

session_file="${TEMP_DIR}/${REQUEST_UUID}"
cat "${session_file}" && rm -rf "${session_file}"
