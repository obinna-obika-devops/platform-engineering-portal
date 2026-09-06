from fastapi.testclient import TestClient

from portal.api import app

client = TestClient(app)


def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_dev_plan_uses_catalog_template():
    response = client.post(
        "/provision/plan",
        json={"name": "orders", "runtime": "python", "environment": "dev"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["template"] == "python-service"
    assert body["owner"] == "platform-team"
    assert "repository" in body["artifacts"]
    assert body["approval_required"] is False
    assert len(body["plan_id"]) == 12


def test_python_prod_requires_approval():
    response = client.post(
        "/provision/plan",
        json={"name": "orders", "runtime": "python", "environment": "prod"},
    )
    assert response.status_code == 200
    assert response.json()["approval_required"] is True


def test_go_prod_rejected_by_catalog():
    response = client.post(
        "/provision/plan",
        json={"name": "payments", "runtime": "go", "environment": "prod"},
    )
    assert response.status_code == 400
    assert "not enabled" in response.json()["detail"]


def test_unknown_runtime_rejected():
    response = client.post(
        "/provision/plan",
        json={"name": "payments", "runtime": "node", "environment": "dev"},
    )
    assert response.status_code == 400
    assert "unsupported golden-path runtime" in response.json()["detail"]


def test_invalid_service_name_rejected():
    response = client.post(
        "/provision/plan",
        json={"name": "Bad Service", "runtime": "python", "environment": "dev"},
    )
    assert response.status_code == 422


def test_plan_id_is_deterministic():
    payload = {"name": "orders", "runtime": "python", "environment": "dev"}
    first = client.post("/provision/plan", json=payload).json()["plan_id"]
    second = client.post("/provision/plan", json=payload).json()["plan_id"]
    assert first == second
