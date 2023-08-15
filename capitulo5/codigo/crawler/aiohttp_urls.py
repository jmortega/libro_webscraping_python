import aiohttp
import asyncio

async def fetchWithErrors(session, url):
	try:
		async with session.get(url) as response:
			print('Status: '+str(response.status))
			if response.status != 200:
				print(response.reason)
			return await response.text()
	except Exception as e:
		print(e.strerror)
            
async def fetch(session, url):
    async with session.get(url) as response:
        print(response.status == 200)
        return await response.text()
            
async def fetch_all(session, urls):
    results = await asyncio.gather(
        *[fetchWithErrors(session, url) for url in urls],
        return_exceptions=True  # default is false, that would raise
    )
    # gather returns results in the order of coros
    for idx, url in enumerate(urls):
        print('{}: {}'.format(url, 'ERR' if isinstance(results[idx], Exception) else 'OK'))
    return results

async def main(urls):
    async with aiohttp.ClientSession() as session:
        await fetch_all(session, urls)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    urls = [
        'http://other_domain.com',
        'http://www.google.com',
        'http://www.python.org']
    try:
        loop.run_until_complete(main(urls))
    except Exception as e:
        print('Exception'+ str(e))
        pass
