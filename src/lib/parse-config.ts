import { readFile } from "node:fs/promises"
import { parse } from 'yaml'

export type HttpMethod = 'POST' | 'GET' | 'PUT' | 'DELETE' | 'PATCH'

export type Route = {
  /**
   * Regular expression to match the path to
   */
  path: string | RegExp
  method: HttpMethod,
  /**
   * The path to the controller/handler script for the route
   */
  controller: string 
}

export type BashGqlConfigOptions = {
  /**
   * Absolute path to the cgi entry script, likely a router
   */
  routerScript: string,

  /**
   * The port for the cgi server to listen for connections on 
   */
  port: number,

  /**
   * The path to the bash library code
   */
  libDir: string,

  /**
   * The temporary directory used by the bash server to build the HTTP response as a file
   */
  tempDir: string,

  /**
   * route declarations
   */
  routes: Route[]
}

export async function parseConfig(
  filePath: string
): Promise<BashGqlConfigOptions> {
  const yamlFileData = await readFile(filePath)
  const data = parse(yamlFileData.toString()) 

  return data as BashGqlConfigOptions
}
