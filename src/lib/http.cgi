#!/bin/bash
source "${LIB_DIR}/response.cgi"
source "${LIB_DIR}/log.cgi"

function http-header {
  local header_key=$1
  local header_value=$2

  response-write "${header_key}: ${header_value}"
}
export -f http-header

function http-body {
  local body_contents=$1
  response-write-body "${body_contents}"
}
export -f http-body

function http-json-body {
  local json=$(bash -c "jq -cn $* '\$ARGS.named'")
 
  response-write-body "$json"
}
export -f http-json-body
