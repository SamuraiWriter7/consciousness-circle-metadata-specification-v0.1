#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]

SCHEMA_PATH = ROOT / "schemas" / "consciousness-circle-metadata-v0.2.schema.json"

SPEC_PATH = ROOT / "spec" / "consciousness-circle-metadata-specification-v0.2.yaml"

EXAMPLE_PATHS = [
    ROOT / "examples" / "minimal-circle-v0.2.example.yaml",
    ROOT / "examples" / "extended-circle-v0.2.example.yaml",
    ROOT / "examples" / "proto-friction-v0.2.example.yaml",
    ROOT / "examples" / "silence-node-v0.2.example.yaml"
]


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path) -> object:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def format_error_path(error) -> str:
    if not error.path:
        return "<root>"
    return ".".join(str(part) for part in error.path)


def main() -> int:
    print("Validating Consciousness Circle Metadata v0.2 files...")

    if not SCHEMA_PATH.exists():
        print(f"ERROR: Schema not found: {SCHEMA_PATH}")
        return 1

    if not SPEC_PATH.exists():
        print(f"ERROR: Specification not found: {SPEC_PATH}")
        return 1

    schema = load_json(SCHEMA_PATH)

    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        print("ERROR: JSON Schema itself is invalid.")
        print(exc)
        return 1

    print(f"OK: Schema is valid JSON Schema Draft 2020-12: {SCHEMA_PATH.relative_to(ROOT)}")

    try:
        spec = load_yaml(SPEC_PATH)
    except Exception as exc:
        print(f"ERROR: Failed to parse spec YAML: {SPEC_PATH.relative_to(ROOT)}")
        print(exc)
        return 1

    if not isinstance(spec, dict):
        print(f"ERROR: Spec YAML must parse into an object: {SPEC_PATH.relative_to(ROOT)}")
        return 1

    print(f"OK: Spec YAML parsed: {SPEC_PATH.relative_to(ROOT)}")

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker()
    )

    failed = False

    for example_path in EXAMPLE_PATHS:
        if not example_path.exists():
            print(f"ERROR: Example not found: {example_path.relative_to(ROOT)}")
            failed = True
            continue

        try:
            instance = load_yaml(example_path)
        except Exception as exc:
            print(f"ERROR: Failed to parse example YAML: {example_path.relative_to(ROOT)}")
            print(exc)
            failed = True
            continue

        errors = sorted(
            validator.iter_errors(instance),
            key=lambda e: list(e.path)
        )

        if errors:
            failed = True
            print(f"\nERROR: Validation failed: {example_path.relative_to(ROOT)}")
            for error in errors:
                print(f"  - Path: {format_error_path(error)}")
                print(f"    Message: {error.message}")
        else:
            print(f"OK: Example validates: {example_path.relative_to(ROOT)}")

    if failed:
        print("\nValidation failed.")
        return 1

    print("\nAll v0.2 examples validated successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
