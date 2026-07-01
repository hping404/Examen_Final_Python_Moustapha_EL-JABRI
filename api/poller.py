import asyncio
import httpx
from api.models import Server


async def poll_server(server: Server):
    url = f"{server.base_url()}{server.health_path}"

    try:
        async with httpx.AsyncClient(timeout=5) as client:
            r = await client.get(url)

        if r.status_code == 200:
            server.status = "UP"
        elif r.status_code < 500:
            server.status = "DEGRADED"
        else:
            server.status = "DOWN"

    except Exception:
        server.status = "DOWN"


async def run_poll_loop(servers: list[Server]):
    while True:
        await asyncio.gather(*(poll_server(s) for s in servers))
        await asyncio.sleep(10)
