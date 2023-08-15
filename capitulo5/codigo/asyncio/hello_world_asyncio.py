import asyncio 

async def main():
	print("Hola mundo")
	await asyncio.sleep(1)
	print("desde asyncio")
    
#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())
#loop.close()

asyncio.run(main())
