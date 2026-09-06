# Platform Engineering Portal

<p align="center"><strong>Self-service infrastructure with guardrails and golden paths.</strong></p>

<p align="center">
<a href="https://github.com/obinna-obika-devops/platform-engineering-portal/actions/workflows/ci.yml"><img src="https://github.com/obinna-obika-devops/platform-engineering-portal/actions/workflows/ci.yml/badge.svg" alt="Platform CI"></a>
<img src="https://img.shields.io/badge/Internal%20Developer%20Platform-IDP-1f6feb" alt="IDP">
<img src="https://img.shields.io/badge/FastAPI-Python-009688?logo=fastapi" alt="FastAPI">
<img src="https://img.shields.io/badge/GitOps-Ready-EF7B4D" alt="GitOps">
<img src="https://img.shields.io/badge/Terraform-Integrated-7B42BC?logo=terraform" alt="Terraform">
</p>

A self-service Internal Developer Platform reference implementation. Developers describe a service request once; the platform validates policy, renders a golden path, and produces artifacts for GitOps/Terraform workflows.

## Developer flow

```mermaid
flowchart LR
    A[Developer] --> B[Platform API]
    B --> C[Service Catalog]
    C --> D[Golden Path]
    D --> E[Policy Gate]
    E --> F[Provisioning Plan]
    F --> G[GitOps / Terraform Artifacts]
    G --> H[Audit Event]
```

## Evidence at a glance

| Engineering concern | Evidence in this repository |
|---|---|
| Developer-facing control plane | FastAPI service and request handling |
| Golden paths | Service catalog and reusable platform templates |
| Guardrails | Policy-aware validation and approval boundaries |
| Provisioning integration | Terraform and GitOps artifact generation |
| Developer experience | CLI-driven self-service workflow |
| Quality | Automated tests and [GitHub Actions CI](.github/workflows/ci.yml) |
| Auditability | Provisioning plans and audit-event flow |

## Platform contract

**Self-service does not mean unrestricted access.** The portal provides a controlled path from developer intent to infrastructure artifacts while preserving policy and approval boundaries.

## Features

- Service catalog and golden-path templates
- Environment/runtime validation
- Policy-aware provisioning plans
- GitOps and Terraform integration points
- Audit events and approval boundaries
- Developer CLI
- Unit tests + CI

## Engineering components

- API/service code — developer request and validation flow
- catalog/golden-path logic — reusable platform abstractions
- policy/provisioning logic — guardrails and approval boundaries
- tests + `.github/` — automated quality and CI validation

## Technology

| Layer | Stack |
|---|---|
| API | FastAPI / Python |
| Platform | Service catalog / golden paths |
| Infrastructure | Terraform integration |
| Delivery | GitOps integration |
| Governance | Policy gates / approval boundaries |
| Quality | Pytest / GitHub Actions |

## Quick start

```bash
pip install -r requirements.txt
pytest -q
```

No external repositories or cloud accounts are modified automatically by this reference implementation.

## Design principle

The core platform-engineering objective is to **reduce developer cognitive load without hiding infrastructure, security, governance, or operational responsibilities.**

## Scope

This is a portfolio/reference implementation. It demonstrates platform-engineering design and automation without claiming a live enterprise deployment or production usage that is not explicitly evidenced in the repository.
