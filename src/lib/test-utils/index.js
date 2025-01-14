const { spawn } = require("node:child_process")
const { resolve } = require('node:path')
const { exec } = require("promisify-child-process")

const ENV = 'local'
const BASE_URL = 'localhost:8888'

function getHomePath(env) {
  switch(this.env) {
    case 'local':
    default:
      return resolve(`${process.env.HOME}/Projects/gql-bash-plus-unity`)
  }
}

function mapHeaders(rawHeaders) {
  const headers = new Headers()
  console.log('rawHeaders: ', rawHeaders)
  rawHeaders.forEach((header, i) => {
    if(i === 0) return
    const [k, v] = header
    console.log(k, v)
    headers.append(k, v)
  })

  return headers
}

async function sendCurlRequest(path) {
  const { stdout, stderr } = await exec(`curl -si ${BASE_URL}${path}`)

  if(stderr) {
    throw new Error(`Error: failed to execute cURL command for ${BASE_URL}${path}\n${stderr}`)
  }

  return stdout
    .split(/\r\n\r\n/)
    .reduce((acc, curr, i) => { 
      curr = curr.trim()
      console.log(curr)
      if(i === 1) {
        console.log(curr)
        return { ...acc, body: curr}
      }

      curr.split(/\n/).forEach((line, i) => {
        if(i === 0) {
          acc.status = line.split(/\s/)[1]
        }

        const [k, v] = line.split(/\:\s/)
        const isValidHeader = !!k && !!v
        isValidHeader && acc.headers.set(k, v) 
      })

     return acc
    }, { headers: new Headers(), body: null, status: null })
}

module.exports = {
    sendCurlRequest
}