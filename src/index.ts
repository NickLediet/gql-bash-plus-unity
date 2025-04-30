
import cgi from 'cgi'
import { createServer } from 'node:http'
import path from 'path'
import { cwd } from 'process'
import { parseConfig } from './lib/parse-config.ts'
import { read, readFileSync } from 'node:fs'
import { v4 as uuid } from 'uuid'
import { stderr } from 'node:process'
import { exec } from 'node:child_process'

function setupServer(script: string, port: number) {
    const cgiHandler = cgi(script, { stderr })

    const server = createServer((...args) => {
      process.env.REQUEST_UUID = uuid()
      return cgiHandler(...args)
    })

    // @TODO: replace with an actual logger
    server.on('error', console.error)
    server.listen(port, () => {
      console.log(`Starting server on port ${port}`)
    })  
}

(async function main() {
  try {
    const config = await parseConfig("bashgql.yaml")
    const port = (config.port || process.env.PORT || 8888) as number
    const srcDir = config.srcDir
    const script = path.resolve(
      srcDir,
      config.entryScript
    )
    process.env.BASHGQL_CONFIG = JSON.stringify(config)
    process.env.LIB_DIR = config.libDir
    process.env.TEMP_DIR = path.resolve(config.tempDir)
    process.env.SRC_DIR = srcDir
    process.env.GRAPHQL_ENDPOINT = config.graphql_endpoint
    process.env.GRAPHQL_METHOD = config.graphql_method
    process.env.GRAPHQL_REQUIRE_RESPONSE_HEADER = config.graphql_require_response_header.toString()

    setupServer(script, port)
  } catch (error) {
    if(!(error instanceof Error)) {
      // @TODO: replace with logger
      console.error("Unknown error thrown: ", error)
      process.exit(1)
    }

    // @TODO: Replace with logger
    console.error("Error: ", error.message)
    process.exit(1);
  }
})()


