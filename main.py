import asyncio
import time
import aiohttp
import requests


async def main():
    urls = ['https://google.com'] * 10
    async with aiohttp.ClientSession() as session:
        tasks = [
            session.get(url) for url in urls
        ]
        results = await asyncio.gather(*tasks)
        print(list(map(lambda x: x.status, results)))
asyncio.run(main())