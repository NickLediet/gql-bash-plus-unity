
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
    const script = path.resolve(
      config.routerScript
    )
    process.env.BASHGQL_CONFIG = JSON.stringify(config)
    process.env.LIB_DIR = config.libDir
    process.env.TEMP_DIR = path.resolve(config.tempDir)

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


