import asyncio
import json
import uuid
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, WebSocket, WebSocketDisconnect, HTTPException

from api.models import Server, ServerIn, ServerOut
from api.metrics import get_system_metrics
from api.auth import verify_api_key
from api.poller import run_poll_loop

servers: dict[str, Server] = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(run_poll_loop(list(servers.values())))
    yield
    task.cancel()


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metrics")
def metrics():
    return get_system_metrics()


@app.post("/servers", dependencies=[Depends(verify_api_key)])
def add_server(server: ServerIn):
    sid = str(uuid.uuid4())
    s = Server(id=sid, **server.model_dump())
    servers[sid] = s
    return ServerOut(id=s.id, status=s.status, **server.model_dump())


@app.get("/servers")
def list_servers():
    return [
        ServerOut(
            id=s.id,
            name=s.name,
            host=s.host,
            port=s.port,
            protocol=s.protocol,
            health_path=s.health_path,
            status=s.status,
        )
        for s in servers.values()
    ]


@app.delete("/servers/{server_id}", dependencies=[Depends(verify_api_key)])
def delete_server(server_id: str):
    if server_id not in servers:
        raise HTTPException(404, "Server not found")
    del servers[server_id]
    return {"deleted": server_id}


@app.post("/servers/{server_id}/check", dependencies=[Depends(verify_api_key)])
async def check_server(server_id: str):
    if server_id not in servers:
        raise HTTPException(404)

    from api.poller import poll_server
    await poll_server(servers[server_id])
    return {"status": servers[server_id].status}


@app.websocket("/ws/metrics")
async def ws_metrics(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            await ws.send_text(json.dumps(get_system_metrics()))
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        pass
