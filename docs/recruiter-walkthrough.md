# Recruiter / Interview Walkthrough

This page highlights the platform-engineering signal in this repository.

## 5-minute review path

1. Read `README.md` for the developer flow and platform contract.
2. Inspect the API/service code for how developer requests are accepted and validated.
3. Inspect catalog and golden-path logic for reusable service patterns.
4. Inspect policy and provisioning logic for guardrails and approval boundaries.
5. Inspect tests and `.github/` for quality gates and CI.

## What this project proves

The portal is built around a core platform-engineering idea: developers should get a simple self-service path without bypassing infrastructure, security or governance controls.

The project demonstrates:

- internal developer platform concepts
- self-service infrastructure requests
- service catalog and golden paths
- policy-aware provisioning plans
- Terraform and GitOps integration points
- developer experience through API/CLI patterns
- auditability and approval boundaries
- Python testing and CI

## Interview discussion points

### Why use a golden path?
A golden path gives developers a supported, repeatable way to create services while embedding the organization’s reliability, security and operational defaults. It reduces cognitive load without removing engineering controls.

### Why keep approval boundaries?
Self-service should automate low-risk, repeatable work, while high-impact actions remain subject to policy or human approval. This prevents convenience from becoming unrestricted infrastructure access.

### How would this scale in a larger company?
The catalog would typically integrate with identity, ownership metadata, source control, CI/CD, cloud accounts/subscriptions, secrets management, observability and a service catalog such as Backstage or an internal equivalent.

### What would be added for production?
Productionization would include persistent storage, authenticated users, role-based authorization, external policy engines, durable audit events, real provisioning backends, idempotency, rate limiting, tracing and HA deployment.

## Validation

```bash
pip install -r requirements.txt
pytest -q
```

Use the repository CI workflow for automated validation.

## Scope and integrity

This is a portfolio/reference implementation. It demonstrates how an internal developer platform can be structured without claiming a live enterprise deployment or production usage that is not evidenced in the repository.
