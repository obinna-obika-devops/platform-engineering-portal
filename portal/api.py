from hashlib import sha256

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from portal.catalog import validate_selection

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
        template, entry = validate_selection(req.runtime, req.environment)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    approval_required = req.environment == "prod"
    plan_key = f"{req.name}:{template}:{req.environment}"
    plan_id = sha256(plan_key.encode()).hexdigest()[:12]

    artifacts = [
        "repository",
        "ci-pipeline",
        "k8s-manifest",
        "gitops-registration",
    ]

    return {
        "plan_id": plan_id,
        "service": req.name,
        "runtime": req.runtime,
        "template": template,
        "environment": req.environment,
        "owner": entry["owner"],
        "artifacts": artifacts,
        "approval_required": approval_required,
        "policy": {
            "catalog_enforced": True,
            "production_approval": approval_required,
        },
    }
