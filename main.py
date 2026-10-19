import asyncio

async def get_message():
    return 'Hello!'

async def main():
    result =  await asyncio.create_task(get_message())
    print('Hello!', result)

asyncio.run(main())