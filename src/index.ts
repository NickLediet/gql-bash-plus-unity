
import cgi from 'cgi'
import { createServer } from 'node:http'
import path from 'path'
import { cwd } from 'process'

// @TODO: migrate to yaml config w/defauts
const PORT = process.env.PORT || 8888

// @TODO: migrate to yaml config w/defauts
const script = path.resolve('src/router.cgi')

console.log(script)

const server = createServer(
  cgi(script)
)


// @TODO: replace with an actual logger
server.on('error', console.error)


server.listen(PORT, () => {
  console.log(`Starting server on port ${PORT}`)
})
