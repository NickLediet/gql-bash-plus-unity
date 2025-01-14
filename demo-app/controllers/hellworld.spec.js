const { sendCurlRequest } = require('../../src/lib/test-utils')

describe('GET / (helloworld enpoint)', () => {
  it('200 -> sucessful response', async () => {
    const { status, headers, body } = await sendCurlRequest('/')
    expect(status).toBe('200')
    expect(headers.get('Content-Type')).toBe('text/plain')
    expect(body).toBe('Hello World!')
  })
})
