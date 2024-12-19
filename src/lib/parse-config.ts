import { readFile } from "node:fs/promises"
import { parse } from 'yaml'

export type BashGqlConfigOptions = {
  /**
   * Absolute path to the cgi entry script, likely a router
   */
  routerScript: string,

  /**
   * The port for the cgi server to listen for connections on 
   */
  port: number
}

export async function parseConfig(
  filePath: string
): Promise<BashGqlConfigOptions> {
  const yamlFileData = await readFile(filePath)
  const data = parse(yamlFileData.toString()) 

  return data as BashGqlConfigOptions
}
