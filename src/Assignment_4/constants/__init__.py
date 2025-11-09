from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

Config_yaml_path = PROJECT_ROOT / "config" / "config.yaml"
schema_yaml_path = PROJECT_ROOT / "schema.yaml"
params_yaml_path = PROJECT_ROOT / "params.yaml"