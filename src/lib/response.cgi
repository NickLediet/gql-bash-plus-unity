#!/bin/bash
# Builds the temp dir if required to hold response temp files
function response-dir-create {
  if [[ ! -d "${TEMP_DIR}" ]]; then
    mkidr "${TEMP_DIR}"
  fi
}
export -f response-dir-create

# Creates the response temp file for this HTTP Response
function response-create {
  response-dir-create
  
  if [[ ! -f "${TEMP_DIR}/${REQUEST_UUID}" ]]; then
    touch "${TEMP_DIR}/${REQUEST_UUID}"
  fi
}
export -f response-create

# Writes arg string to new line in the HTTP Response file
function response-write {
  echo $1 >> "${TEMP_DIR}/${REQUEST_UUID}"
}
export -f response-write

# Write an empty line + new lines for the provide args for the HTTP Response file's body
function response-write-body {
  data=$1
  echo >> "${TEMP_DIR}/${REQUEST_UUID}"
  echo "${data}" >> "${TEMP_DIR}/${REQUEST_UUID}"
}
export -f response-write-body

# Reads the contents for the HTTP Response
function response-read {
  cat "${TEMP_DIR}/${REQUEST_UUID}"
}
export -f response-read

