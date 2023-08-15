import asyncio
from aiohttp import ClientSession

async def fetch(url, session):
    async with session.get(url) as response:
        return await response.read()
		
def print_responses(result):
    print(result)
	
async def execute(loop):
    url = "http://www.python.org/{}"
    tasks = []
    sites = ['about','downloads','doc','community','blog','events']
    async with ClientSession() as session:
    	for site in sites:
    		task = asyncio.ensure_future(fetch(url.format(site), session))
    		tasks.append(task)
    	responses = await asyncio.gather(*tasks)
    	print(responses)
		
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(execute(loop))
loop.run_until_complete(future)
