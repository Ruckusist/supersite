import aiohttp
from colorama import Fore
# from aiohttp import WSMsgType, WSMessage, ClientSession, web

# websocket server
def handle_msg(msg: str) -> bool:
    print(f"[MSG] {msg}")
    return True

async def socket_server(request) -> None:
    ws = aiohttp.web.WebSocketResponse()
    await ws.prepare(request)
    try:
        msg: aiohttp.WSMessage
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                # if not handle_msg(msg.json()):
                if not handle_msg(msg.data):
                    print("did this fail?")
                    break
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print(Fore.YELLOW + "Connection error: " + msg.data + Fore.RESET)
            elif msg.type == aiohttp.WSMsgType.CLOSE:
                print(Fore.YELLOW + "Server closed connection" + Fore.RESET)
    except asyncio.CancelledError: pass
