import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)
    print("Data fetched.")

# Create an event loop and run the coroutine
asyncio.run(fetch_data())