import asyncio

async def task1():
    print("Task 1 running...")
    await asyncio.sleep(1)
    print("Task 1 done.")

async def task2():
    print("Task 2 running...")
    await asyncio.sleep(2)
    print("Task 2 done.")

async def main():
    # Run both tasks concurrently
    await asyncio.gather(task1(), task2())

# Run the event loop
asyncio.run(main())