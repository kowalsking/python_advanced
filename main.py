import asyncio

async def job():
    print('Working')
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
        
        
asyncio.run(main())