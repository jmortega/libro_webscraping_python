import asyncio  
import aiohttp
async def realizar_peticion():  
    url = "http://www.python.org"
    print(f"Realizando petición a la url {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                print(await resp.text())

loop = asyncio.get_event_loop()  
loop.run_until_complete(realizar_peticion())  

