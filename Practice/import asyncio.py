import asyncio
async def mySleep(second: int):
    print(f"going to sleep for {second}s ...")
    await asyncio.sleep(second)
    print(f"... back after {second}s")
async def main():
    task1 = asyncio.create_task(mySleep(5))
    task2 = asyncio.create_task(mySleep(3))
    task3 = asyncio.create_task(mySleep(1))
    await task1
    await task2
    await task3
asyncio.run(main())