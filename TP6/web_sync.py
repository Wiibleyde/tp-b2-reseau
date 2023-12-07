import requests
import sys

def getPage(url:str) -> str:
    try:
        r = requests.get(url)
        return r.text
    except:
        return ""
    
def saveToFile(path='/tmp/web_page', content:str=''):
    with open(path, 'w') as f:
        f.write(content)

    
if __name__=='__main__':
    if len(sys.argv) != 2:
        print("Usage: python web_sync.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    content = getPage(url)
    saveToFile(content=content)