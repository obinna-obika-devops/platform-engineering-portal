from functools import lru_cache
from pathlib import Path

import yaml

CATALOG_PATH = Path(__file__).resolve().parent.parent / "catalog" / "services.yaml"


@lru_cache(maxsize=1)
def load_catalog() -> dict[str, dict]:
    data = yaml.safe_load(CATALOG_PATH.read_text()) or {}
    services = data.get("services", [])
    catalog: dict[str, dict] = {}
    for item in services:
        template = item.get("template")
        if not template:
            raise ValueError("catalog service template is required")
        catalog[template] = {
            "owner": item.get("owner", "unknown"),
            "environments": set(item.get("environments", [])),
        }
    return catalog


def resolve_template(runtime: str) -> str:
    return f"{runtime}-service"


def validate_selection(runtime: str, environment: str) -> tuple[str, dict]:
    template = resolve_template(runtime)
    catalog = load_catalog()
    if template not in catalog:
        raise ValueError("unsupported golden-path runtime")
    entry = catalog[template]
    if environment not in entry["environments"]:
        raise ValueError("environment is not enabled for selected golden path")
    return template, entry
