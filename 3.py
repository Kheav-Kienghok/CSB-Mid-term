import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [
        'https://www.aupp.edu.kh/',
        'https://www.cadt.edu.kh/',
        'https://paragoniu.edu.kh/'
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        
        for response in responses:
            print(response)

# Complete the code to run the async function
if __name__ == "__main__":
    asyncio.run(main())