#!/bin/bash
source "${LIB_DIR}/config-query.cgi"
source "${LIB_DIR}/log.cgi"
source "${LIB_DIR}/graphql/parse-resolvers.cgi"
function strip-quotes {
  if [[ -z "$1" ]]; then
    read -r data
  else
    data=$1
  fi

  echo "${data}" | sed 's/\"//g'
}

function json-query {
  local jq_selector=$1
  local json_contents=$2
  echo "${json_contents}" | jq "fromjson | ${jq_selector}"
}

function router-process {
  local jq_select_by_http_method="select(.method == \"${REQUEST_METHOD}\")"
  local jq_select_matching_routes=".routes[] | ${jq_select_by_http_method}"
  local routes=$(config-query "${jq_select_matching_routes} | tostring")
  
  log "Resolving route for request \"${REQUEST_METHOD} ${PATH_INFO}\""
  log "=> graphql endpoint: ${GRAPHQL_ENDPOINT}"
  log "=> graphql method: ${GRAPHQL_METHOD}"
  log "=> graphql require response header: ${GRAPHQL_REQUIRE_RESPONSE_HEADER}"
  if [[ "${PATH_INFO}" =~ ${GRAPHQL_ENDPOINT} && "${REQUEST_METHOD}" == "${GRAPHQL_METHOD}" ]]; then
    log "=> invoking graphql resolver reconciliation"
    parse-resolvers
    return 0
  fi
  
  for route_data in $routes; do
    local route=$(json-query ".route" "${route_data}")
    local clean_path=$(strip-quotes "${route}")

    if [[ "${PATH_INFO}" =~ $clean_path ]]; then
      local controller=$(json-query ".controller" "${route_data}" | strip-quotes)
      log "=> invoking controller ${controller}"
      source "${SRC_DIR}/${controller}"
    fi
  done
}
export -f router-process
