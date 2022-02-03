import os, asyncio
from colorama import Fore
import aiohttp
from aiohttp import WSMsgType, WSMessage, ClientSession
from aiohttp import web
import aiohttp_jinja2
import jinja2

from src.pages import pages
from src.sock import socket_server


# views
@aiohttp_jinja2.template('main.html')
async def main(request):
    print(Fore.GREEN + f"[REQ] home_page <- {request.remote}" + Fore.RESET)
    return {
        "my_list": ["this", "that?", "other?", "so_what!!!"],
        "requesting_ip": request.remote,
        "pages": pages
    }

# routes
def setup_routes(app):
    app.router.add_get('/', main)
    app.router.add_get('/connect', socket_server)
    app.router.add_static(
        '/static', 
        # "./static", 
        os.path.join(os.getcwd(), 'static'),
        follow_symlinks=True)

# application
def start():
    app = web.Application()
    aiohttp_jinja2.setup(
        app,
        loader = jinja2.FileSystemLoader(
            'templates'
        )
    )
    setup_routes(app)
    web.run_app(app, port=5000)


if __name__ == '__main__':
    start()