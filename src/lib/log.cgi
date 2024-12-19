#!/bin/bash

function create-log {
  if [[ ! -d "${TEMP_DIR}" ]]; then
    mkdir "${TEMP_DIR}"
  fi

  if [[ ! -f "${TEMP_DIR}/log.txt" ]]; then
    touch "${TEMP_DIR}/log.txt"
  fi  
}
export -f create-log

function log {
  create-log 
  if [[ -z "$1" ]]; then
    read -r data
  else
    data=$1
  fi
  echo $data >> "${TEMP_DIR}/log.txt"
}
export -f log

function log-file {
  create-log
  cat $1 >> "${TEMP_DIR}/log.txt"
}
export -f log-file

