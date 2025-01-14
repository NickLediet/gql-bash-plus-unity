# syntax=docker/dockerfile:1

ARG NODE_VERSION=23.4.0

FROM node:${NODE_VERSION}-bookworm as base
WORKDIR /usr/src/app
EXPOSE 8888

FROM base as dev
RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=cache,target=/root/.npm \
    npm ci --include=dev
USER node
COPY . .
CMD npm run start

FROM base as test
# Install cURL for e2e testing
RUN apt-get install curl
    # Install Bash unit for testing
RUN curl -s https://raw.githubusercontent.com/pgrange/bash_unit/master/install.sh | bash
RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=cache,target=/root/.npm \
    npm ci --include=dev
USER node
RUN chown node:node -R ./*
RUN chmod 777 temp-dir/*
COPY . .
CMD echo "whoami:" && whoami && ls -la && npm run test

FROM base as prod
RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=cache,target=/root/.npm \
    npm ci --omit=dev
USER node
COPY . .
CMD npm run start
