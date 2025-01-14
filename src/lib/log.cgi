#!/bin/bash

function create-log {
  if [[ ! -d "${TEMP_DIR}" ]]; then
    mkdir "${TEMP_DIR}"
  fi

  local logfile="${TEMP_DIR}/log.txt"
  if [[ ! -f $logFile ]]; then
    touch "$logfile"
    chmod +w "$logfile"
  fi  
}
export -f create-log

function log {
  if [ "$LOGGING" = "off" ]; then 
    return 0
  fi

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

