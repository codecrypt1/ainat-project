import asyncio
import websockets

async def hello(websocket) :
    res = await websocket.recv()
    print(f"Server received: {res}")
    
    await websocket.send(res)
    print(f"Server sent: {res}")
    
async def main() :
    async with websockets.serve(hello, "localhost", 8000) :
        await asyncio.Future()

if __name__ == "__main__" :
    asyncio.run(main())