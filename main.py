import asyncio

async def good():
    print('Started good')
    return 1

async def bad():
    print('Started')
    raise ValueError('Error')


async def main():
    try:
        result = await asyncio.gather(bad(), good(), return_exceptions=True)
        print(result)
    except ValueError as e:
        print(e)
asyncio.run(main())