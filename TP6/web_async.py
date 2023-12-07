import aiofiles
import aiohttp
import sys
import asyncio

async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            return content
        
async def saveToFile(path='/tmp/web_page', content:str=''):
    async with aiofiles.open(path, 'w') as f:
        await f.write(content)

async def main(url):
    content = await download(url)
    await saveToFile(content=content)

if __name__=='__main__':
    if len(sys.argv) != 2:
        print("Usage: python web_async.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    asyncio.run(main(url))