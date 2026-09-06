import argparse
import json

from portal.planner import build_plan


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a platform provisioning plan")
    parser.add_argument("name")
    parser.add_argument("runtime")
    parser.add_argument("environment")
    args = parser.parse_args()

    try:
        plan = build_plan(args.name, args.runtime, args.environment)
    except ValueError as exc:
        parser.error(str(exc))

    print(json.dumps(plan, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
