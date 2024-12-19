#!/bin/bash
function config-query {
  local jq_selector=$1
  echo "${BASHGQL_CONFIG}" | jq "${jq_selector}"
}
export -f config-query
