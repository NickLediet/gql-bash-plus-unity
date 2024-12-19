#!/bin/bash
source "${LIB_DIR}/response.cgi"

function http_header {
  local header_key=$1
  local header_value=$2

  response_write "${header_key}: ${header_value}"
}
export -f http_header

function http_body {
  local body_contents=$1
  response_write_body "${body_contents}"
}
export -f http_body
