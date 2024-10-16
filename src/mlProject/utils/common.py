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
def read_yaml(path_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_yaml (str): path like input

    Raises:
        ValueError: if yamnl file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_directories: list, verbose = True):
    """"create list of directories

    Args:
        path_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created, default to false.
    """

    for path in path_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):

    """save json data
    
    Args:
        path (Path): path to json file
        data (dict): data to save in json file
    """

    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)

    logger.info(f"json file saved at {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data
    
    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """

    with open(path) as json_file:
        content = json.load(json_file)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data tyo be saved as binary
        path (Path): path to binary file
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load a binary file
    
    Args:
        path (Path): path to binay file

    Returns:
        Any: object stored in the file
    """

    data = joblib.load(path)
    logger.info(f"binary file load from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    
    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"