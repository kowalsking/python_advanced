import asyncio

async def save():
    print('Saving')
    await asyncio.sleep(2)
    print('Saved!')

async def job():
    print('Working')
    t = asyncio.create_task(save())
    await asyncio.shield(t)
    await asyncio.sleep(5)
    print('Done!')


async def main():
    task = asyncio.create_task(job())
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print(task.cancelled())
        print('task canceled')
    await asyncio.sleep(4)
        
        
        
asyncio.run(main())