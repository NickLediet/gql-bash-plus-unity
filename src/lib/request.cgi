#!/bin/bash
source "${LIB_DIR}/log.cgi"

# Reads the request body from the request and returns it as a string, or an associative array
function get-request-body {
    local content_length=$CONTENT_LENGTH
    local var_name=$1

    if [ -z "$content_length" ]; then
        return 0
    fi

    read -n "$content_length" "$var_name"
}
export -f get-request-body

