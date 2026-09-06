from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title='Platform Engineering Portal')
class ServiceRequest(BaseModel):
    name: str
    runtime: str
    environment: str

ALLOWED = {'python','node','go'}
ENVS = {'dev','staging','prod'}

@app.post('/provision/plan')
def plan(req: ServiceRequest):
    if req.runtime not in ALLOWED or req.environment not in ENVS:
        raise HTTPException(400, 'unsupported golden-path selection')
    return {'service': req.name, 'runtime': req.runtime, 'environment': req.environment,
            'artifacts':['repository','ci-pipeline','k8s-manifest','gitops-registration'],
            'approval_required': req.environment == 'prod'}
