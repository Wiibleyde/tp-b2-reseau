import requests

def getPage(url:str) -> str:
    try:
        r = requests.get(url)
        return r.text
    except:
        return ""
    

def saveToFile(name:str, content:str, path='/tmp/web_'):
    with open(path+name, 'w') as f:
        f.write(content)

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

if __name__=='__main__':
    urls = openFile('./TP6/urls.txt')
    for url in urls:
        url = formatUrl(url)
        name = getName(url)
        content = getPage(url)
        saveToFile(name, content)
