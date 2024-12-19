#!/bin/bash
source "${LIB_DIR}/config_query.cgi"

# Builds the temp dir if required to hold response temp files
function response_dir_create {
  if [[ ! -d "${TEMP_DIR}" ]]; then
    mkidr "${TEMP_DIR}"
  fi
}
export -f response_dir_create

# Creates the response temp file for this HTTP Response
function response_create {
  response_dir_create
  
  if [[ ! -f "${TEMP_DIR}/${REQUEST_UUID}" ]]; then
    touch "${TEMP_DIR}/${REQUEST_UUID}"
  fi
}
export -f response_create

# Writes arg string to new line in the HTTP Response file
function response_write {
  echo $1 >> "${TEMP_DIR}/${REQUEST_UUID}"
}
export -f response_write

# Write an empty line + new lines for the provide args for the HTTP Response file's body
function response_write_body {
  echo >> "${TEMP_DIR}/${REQUEST_UUID}"
  echo $1 >> "${TEMP_DIR}/${REQUEST_UUID}"
}
export -f response_write_body

# Reads the contents for the HTTP Response
function response_read {
  cat "${TEMP_DIR}/${REQUEST_UUID}"
}
export -f response_read

