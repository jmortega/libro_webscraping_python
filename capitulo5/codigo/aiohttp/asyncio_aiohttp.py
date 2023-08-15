import asyncio
from aiohttp import ClientSession

async def request():
    async with ClientSession() as session:
        async with session.get("http://httpbin.org/headers") as response:
            response = await response.read()
            print(response.decode())

loop = asyncio.get_event_loop()
loop.run_until_complete(request())
