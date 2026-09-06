# Platform Engineering Portal

A self-service Internal Developer Platform reference implementation. Developers describe a service request once; the platform validates policy, renders a golden path, and produces artifacts for GitOps/Terraform workflows.

## Flow
`Developer -> FastAPI -> catalog/template -> policy gate -> repo/IaC/GitOps artifacts -> audit event`

## Features
- Service catalog and golden-path templates
- Environment/runtime validation
- Policy-aware provisioning plans
- GitOps and Terraform integration points
- Audit events and approval boundaries
- Developer CLI
- Unit tests + CI

No external repositories or cloud accounts are modified automatically by this reference implementation.