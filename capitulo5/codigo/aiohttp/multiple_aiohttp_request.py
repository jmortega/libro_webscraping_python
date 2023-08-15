import asyncio  
import aiohttp

async def realizar_peticion(session, req_n):  
    url = "https://www.python.org"
    print(f"Realizando peticion {req_n} a la url {url}")
    async with session.get(url) as resp:
        if resp.status == 200:
            await resp.text()

async def main():  
    n_requests = 100
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *[realizar_peticion(session, i) for i in range(n_requests)]
        )

loop = asyncio.get_event_loop()  
loop.run_until_complete(main())  
