import asyncio
import aiohttp
import ssl

url_list = ['https://jsonplaceholder.typicode.com/users/1/posts',
            'https://jsonplaceholder.typicode.com/posts/1/comments',
			'https://jsonplaceholder.typicode.com/albums/1/photos',
			'https://jsonplaceholder.typicode.com/users/1/albums',
			'https://jsonplaceholder.typicode.com/users/1/todos']


async def fetch(session, url):
    async with session.get(url, ssl=ssl.SSLContext()) as response:
        return await response.json()


async def fetch_all(urls, loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        results = await asyncio.gather(*[fetch(session, url) for url in urls], return_exceptions=True)
        return results


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    urls = url_list
    htmls = loop.run_until_complete(fetch_all(urls, loop))
    print(htmls)