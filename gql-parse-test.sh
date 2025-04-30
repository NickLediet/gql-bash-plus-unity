#!/usr/bin/env bash

cat | node -e "process.stdout.write(JSON.stringify(require('graphql').parse(require('fs').readFileSync(0).toString())));"
