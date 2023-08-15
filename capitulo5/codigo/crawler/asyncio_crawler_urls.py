import aiohttp
import asyncio
import time

async def download_file(url):
	print(f'Descarga de la url {url}...')
	async with aiohttp.ClientSession() as session:
		print("URL:",url.encode())
		async with session.get(url) as response:
			content = await response.text()
			print(f"Finalizando descarga...")
			return content

async def write_file(id, content):
	filename = f'async_{id}.html'
	with open(filename, 'wb') as f:
		f.write(content.encode())

async def scrape_task(id, url):
	content = await download_file(url)
	await write_file(id, content)

async def main():
	tasks = []
	for url in enumerate(open('urls.txt').readlines()):
		tasks.append(scrape_task(url[0],url[1].strip()))
	await asyncio.wait(tasks)
 
if __name__ == '__main__':
	t1 = time.perf_counter()
	asyncio.run(main())
	t2 = time.perf_counter() - t1
	print(f'Tiempo ejecución: {t2} segundos')
