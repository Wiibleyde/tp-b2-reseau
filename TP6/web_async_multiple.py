import aiofiles
import aiohttp
import asyncio

async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            return content
        
async def saveToFile(path='/tmp/web_', name:str='', content:str=''):
    async with aiofiles.open(path+name, 'w') as f:
        await f.write(content)

def formatUrl(url:str) -> str:
    if url.startswith('http://') or url.startswith('https://'):
        return url
    else:
        return 'http://' + url
    
def getName(url:str) -> str:
    name = ''.join(c for c in url if c.isalnum() or c == '.')
    name = name.replace('http', '')
    name = name.replace('https', '')
    name = name[1:]
    name = name[:-1]
    name = name.replace('.', '_')
    return name

def openFile(path:str) -> list:
    with open(path, 'r') as f:
        return f.readlines()

async def main(url):
    content = await download(url)
    name = getName(url)
    await saveToFile(name=name, content=content)

if __name__=='__main__':
    urls = openFile('./TP6/urls.txt')
    gather = asyncio.gather(*[main(formatUrl(url)) for url in urls])
    loop = asyncio.get_event_loop()
    loop.run_until_complete(gather)
    loop.close()
