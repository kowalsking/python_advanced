import asyncio
import random

async def unstable():
    await asyncio.sleep(2)
    if random.random() < 0.5:
        raise ValueError('Eror')
    return 'OK'

async def run_with_retry(job, max_retries=3):
    for attempt in range(1, max_retries + 1):
        task = asyncio.create_task(job())
        
        try:
            result = await task
            print(f'Try {attempt}: success => {result}')
            return result
        except Exception as e:
            print(f'Try {attempt}: error -> {e}')

            if attempt == max_retries:
                print('All tries fall')
                return 'ERROR'
            await asyncio.sleep(0.5)
                


async def main():
    result = await run_with_retry(unstable)
    print(f'Summary: {result}')
        
        
        
asyncio.run(main())