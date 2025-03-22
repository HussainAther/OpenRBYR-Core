# scanner_config.py
"""
Load CT scanner configurations from JSON or YAML files.
"""
import json
import yaml
import os

def load_config(filepath):
    """
    Load a scanner configuration file.

    Args:
        filepath (str): Path to the JSON or YAML file.

    Returns:
        dict: Scanner configuration dictionary.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    _, ext = os.path.splitext(filepath)
    with open(filepath, 'r') as f:
        if ext.lower() in ['.json']:
            return json.load(f)
        elif ext.lower() in ['.yml', '.yaml']:
            return yaml.safe_load(f)
        else:
            raise ValueError("Unsupported file format. Use .json or .yaml")

def save_config(config, filepath):
    """
    Save a scanner configuration to a file.

    Args:
        config (dict): Scanner configuration dictionary.
        filepath (str): Output path (.json or .yaml).
    """
    _, ext = os.path.splitext(filepath)
    with open(filepath, 'w') as f:
        if ext.lower() in ['.json']:
            json.dump(config, f, indent=4)
        elif ext.lower() in ['.yml', '.yaml']:
            yaml.safe_dump(config, f)
        else:
            raise ValueError("Unsupported file format. Use .json or .yaml")

if __name__ == "__main__":
    # Example usage
    config = {
        "num_detectors": 180,
        "detector_spacing": 1.0,
        "source_to_detector": 1000,
        "source_to_center": 500
    }

    save_config(config, "scanner_config.yaml")
    loaded = load_config("scanner_config.yaml")
    print("Loaded Config:", loaded)

