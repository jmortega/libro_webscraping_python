from datetime import datetime
import asyncio

async def corutinaB():
	return datetime.utcnow()

async def corutinaA():
	for i in range(3):
		now = await corutinaB()
		print("Today date is %s" %now)
		await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(corutinaA())
loop.close()

