
import cgi from 'cgi'
import { createServer } from 'node:http'
import path from 'path'
import { cwd } from 'process'
import { parseConfig } from './lib/parse-config.ts'

function setupServer(script: string, port: number) {
    const server = createServer(
      cgi(script)
    )

    // @TODO: replace with an actual logger
    server.on('error', console.error)
    server.listen(port, () => {
      console.log(`Starting server on port ${port}`)
    })  
}

(async function main() {
  try {
    const config = await parseConfig("bashgql.yaml")
    const port = config.port || process.env.PORT || 8888

    // @TODO: migrate to yaml config w/defauts
    const script = path.resolve(
      config.routerScript
    )


    setupServer(script, port as number);
    console.log(script)

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


