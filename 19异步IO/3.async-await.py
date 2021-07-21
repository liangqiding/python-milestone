import asyncio

# 把@asyncio.coroutine替换为async；
# 把yield from替换为await。

async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")