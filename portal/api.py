from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from portal.planner import build_plan

app = FastAPI(title="Platform Engineering Portal", version="1.1.0")


class ServiceRequest(BaseModel):
    name: str = Field(pattern=r"^[a-z][a-z0-9-]{1,62}$")
    runtime: str
    environment: str


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.post("/provision/plan")
def plan(req: ServiceRequest):
    try:
        return build_plan(req.name, req.runtime, req.environment)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
