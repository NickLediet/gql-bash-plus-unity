#!/bin/bash
function config_query {
  jq_selector=$1
  echo "${BASHGQL_CONFIG}" | jq "${jq_selector}"
}
export -f config_query
