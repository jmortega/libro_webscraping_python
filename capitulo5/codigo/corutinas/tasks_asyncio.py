import asyncio

async def wait_around(n, name):  
    for i in range(n):
        print(f"{name}: iteration {i}")
        await asyncio.sleep(1.0)

async def main():  
    await asyncio.gather(*[
        wait_around(2, "coroutine 0"), wait_around(5, "coroutine 1")
    ])

loop = asyncio.get_event_loop()  
loop.run_until_complete(main())