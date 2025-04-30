#!/usr/bin/bash
source "${LIB_DIR}/request.cgi"

function parse-gql-request {
    local gql_request=$@
    local node_script="process.stdout.write(JSON.stringify(require('graphql').parse(require('fs').readFileSync(0).toString())));"
    local parse_query=$(cat "$gql_request")
    # parse_query=$(jq '.query' "$gql_request" | node -e "$node_script")
    log "GQL request JSON: $gql_request"
    echo "$parse_query"
}

function parse-resolvers {
    get-request-body gql_request

    # local gql_request_json=$(
    #     echo "$gql_request" |\
    #      jq -r '.query'
    # )
    # log "GQL request JSON: $gql_request_json"

    local gql_query_json=$(
        echo "$gql_request" 
        node -e "process.stdout.write(require('fs').readFileSync(0).toString());"
        # node -e "process.stdout.write(JSON.stringify(require('graphql').parse(require('fs').readFileSync(0).toString())));"
    )
    log "GQL query JSON: $gql_query_json"
    # local gql_request_json=$(jq -rs '.' $gql_request)
    # log "GQL request body: $gql_request"
    # log "GQL request JSON: $gql_request_json"


    # gql_request_json=$(jq '@sh' <$gql_request | parse-gql-request)
    # local resolver_config=$(config-query ".resolvers")
}
export -f parse-resolvers
