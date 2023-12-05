import asyncio

async def compte_jusqua_10():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

if __name__=='__main__':
    loop = asyncio.get_event_loop()
    tasks = [compte_jusqua_10(), compte_jusqua_10()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    
