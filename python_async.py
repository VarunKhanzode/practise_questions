import asyncio
import aiohttp

# asyncio is a Python standard library used to write concurrent code using the async/await syntax.
# It’s a single-threaded, single-process cooperative multitasking library — which means it runs tasks 
# concurrently by switching between them when one is waiting (e.g., for I/O).


# Real-Time Use Case: API Calls in Parallel
# Imagine you're building a backend that fetches data from multiple APIs (e.g., weather, news, finance). Doing them sequentially is slow, so you use asyncio to do them concurrently.

# ✅ Example: Fetch multiple URLs concurrently

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://api.github.com"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response[:100])  # Print first 100 chars

asyncio.run(main())
# Here, all requests are sent at the same time and we wait for all responses concurrently — fast and efficient.




# Test Scenario: Async vs Sync (Comparison)
import time

async def async_task():
    await asyncio.sleep(1)
    return "done"

def sync_task():
    time.sleep(1)
    return "done"

# Async version
start = time.time()
asyncio.run(asyncio.gather(async_task(), async_task(), async_task()))
print("Async took:", time.time() - start)

# Sync version
start = time.time()
sync_task()
sync_task()
sync_task()
print("Sync took:", time.time() - start)

# Output:
# Async took: ~1.0s
# Sync took: ~3.0s