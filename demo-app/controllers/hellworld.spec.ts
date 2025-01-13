import { describe, it } from 'jest'
import { spawn, exec } from 'promisify-child-process'
import { resolve } from 'node:path'
// class DemoAppTestController {
//   private cgiServerProcess: ChildProcess|null;
//
//   public startServer(): void {
//     this.cgiServerProcess = spawn("npm run start") 
//   }
// }


describe('GET / (helloworld enpoint)', () => {
  it('goes green', async () => {
    const { stdout, stderr } = exec('pwd')

    expect(stdout).toBe(resolve('../../'))
  })
})
