// import { describe, it } from 'jest'
// import { spawn, exec } from 'promisify-child-process'
// import { resolve } from 'node:path'

// const { describe, it } = require('jest')
const { spawn, exec } = require('promisify-child-process')
const { resolve } = require('node:path')

const ENV = 'local'
// class DemoAppTestController {
//   cgiServerProcess;

//   constructor(env) {
//     this.env = env
//   }

//   startServer() {
//     this.cgiServerProcess = spawn("npm run start") 
//   }
// }

function getHomePath(env) {
  switch(this.env) {
    case 'local':
    default:
      return resolve(`${process.env.HOME}/Projects/gql-bash-plus-unity`)
  }
}


describe('GET / (helloworld enpoint)', () => {
  it('goes green', async () => {
    const { stdout, stderr } = await exec('pwd')

    console.log({ stdout, path: getHomePath(ENV)})
    expect(stdout.trim()).toBe(getHomePath(ENV))
  })
})
