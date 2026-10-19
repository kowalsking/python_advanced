import asyncio
import time

async def fetch():
    await asyncio.sleep(2)
    return 'done'


async def main():
    tasks = [fetch() for _ in range(3)]
    results = await asyncio.gather(*tasks)
    print(results)
    # for _ in range(3):
    #     print(fetch())

asyncio.run(main())