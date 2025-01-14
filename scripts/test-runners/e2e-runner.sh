#!/bin/bash

export LOGGING="off"
npm start &

sleep 3

npm run test:e2e

kill -9 $(lsof -t -i tcp:8888)