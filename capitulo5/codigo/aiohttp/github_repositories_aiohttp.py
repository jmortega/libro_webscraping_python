import asyncio
import json
import aiohttp

async def github_search(query):
	async with aiohttp.ClientSession() as session:
		async with session.get('https://api.github.com/search/repositories',
                                params={'q': query}) as response:
			return await response.json(loads = json.loads)

loop = asyncio.get_event_loop()
response = loop.run_until_complete(github_search('asyncio'))
print('\n'.join(repo['full_name'] for repo in response['items']))
loop.close()