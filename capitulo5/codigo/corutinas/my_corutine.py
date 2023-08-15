import asyncio

async def my_coroutine():
    print('coroutine called')

#bucle de eventos
loop = asyncio.get_event_loop()

#ejecutar la corutina en el bucle de eventos
loop.run_until_complete(my_coroutine())
loop.close()

