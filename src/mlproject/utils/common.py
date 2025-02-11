import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): path-like input.

    Raises:
        ValueError: if yaml file is empty.

    Returns:
        ConfigBox: ConfigBox object with yaml file contents.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not content:
                raise ValueError("Empty YAML file")
            return ConfigBox(content)
    except Exception as e:
        raise ValueError(f"Error reading YAML file: {e}")

@ensure_annotations
def create_directories(path_to_dict: list, verbose=True):
    for path in path_to_dict:  # Fixed variable name
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")
    
@ensure_annotations
def load_bin(path:Path) -> Any:
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) ->Any:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f" ->{size_in_kb} KB"
