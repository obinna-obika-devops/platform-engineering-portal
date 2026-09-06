from hashlib import sha256

from portal.catalog import validate_selection

ARTIFACTS = (
    "repository",
    "ci-pipeline",
    "k8s-manifest",
    "gitops-registration",
)


def build_plan(name: str, runtime: str, environment: str) -> dict:
    template, entry = validate_selection(runtime, environment)
    approval_required = environment == "prod"
    plan_key = f"{name}:{template}:{environment}"
    plan_id = sha256(plan_key.encode()).hexdigest()[:12]

    return {
        "plan_id": plan_id,
        "service": name,
        "runtime": runtime,
        "template": template,
        "environment": environment,
        "owner": entry["owner"],
        "artifacts": list(ARTIFACTS),
        "approval_required": approval_required,
        "policy": {
            "catalog_enforced": True,
            "production_approval": approval_required,
        },
        "audit_event": {
            "type": "provisioning.plan.created",
            "subject": name,
            "plan_id": plan_id,
        },
    }
