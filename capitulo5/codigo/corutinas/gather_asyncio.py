import asyncio

async def mycoroutine(name):
    print(f'{name} started')
    await asyncio.sleep(1)
    print(f'{name} finished')

if __name__ ==  '__main__':
	
	tasks=[
		asyncio.ensure_future(mycoroutine('first')),
		asyncio.ensure_future(mycoroutine('second')),
		]
	loop = asyncio.get_event_loop()
	
	#we create task and associate it with the loop, executing it
	loop.run_until_complete(asyncio.gather(*tasks))