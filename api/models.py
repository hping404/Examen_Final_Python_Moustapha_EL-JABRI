from dataclasses import dataclass
from pydantic import BaseModel, Field


@dataclass
class Server:
    id: str
    name: str
    host: str
    port: int
    protocol: str
    health_path: str
    status: str = "UNKNOWN"

    def base_url(self):
        return f"{self.protocol}://{self.host}:{self.port}"


class ServerIn(BaseModel):
    name: str
    host: str
    port: int = Field(ge=1, le=65535)
    protocol: str
    health_path: str


class ServerOut(ServerIn):
    id: str
    status: str
