import asyncio

async def sendmail():
    print(f"Sending task 1")
    asyncio.create_task(send())

    asyncio.create_task(print("fooooooooooo"))
    await asyncio.sleep(2)
    print(f"Sending task 1")
async def send():
    print(f"Sending task 2")
    asyncio.create_task(send3())
    await asyncio.sleep(5)
    print(f"Sending task 2")
async def send3():
    print(f"Sending task 3")
    await asyncio.sleep(2)
    print(f"Sending task 3")
asyncio.run(sendmail())