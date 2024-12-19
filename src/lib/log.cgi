#!/bin/bash

function __create_log {
  if [[ ! -d "${TEMP_DIR}" ]]; then
    mkdir "${TEMP_DIR}"
  fi

  if [[ ! -f "${TEMP_DIR}/log.txt" ]]; then
    touch "${TEMP_DIR}/log.txt"
  fi  
}

function __log {
  __create_log 
  echo $1 >> "${TEMP_DIR}/log.txt"
}

function __log_file {
  __create_log
  cat $1 >> "${TEMP_DIR}/log.txt"
}
