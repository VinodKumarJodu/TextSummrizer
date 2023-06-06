import os
import yaml
from TextSummarizer.logging import logger
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object
    :param path_to_yaml: Path to the yaml file
    :raises ValueError:if yaml file is empty
    :return: ConfigBox object
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml_fle:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True)-> None:
    """
    Creates a list of directories
    :param path_to_directories: List of directories
    :param verbose: Prints the directories that are created
    :return: None
    """
    for directory in path_to_directories:
        try:
            os.makedirs(directory, exist_ok=True)
            if verbose:
                logger.info(f"Directory {directory} created successfully")
        except Exception as e:
            raise e
    
@ensure_annotations
def get_size(path_to_file: Path)-> str:
    """
    Returns the size of a file in bytes
    :param path_to_file: Path to the file
    :return: Size of the file in KB
    """
    size_in_kb =round(os.path.getsize(path_to_file)/1024)
    return f"~ {size_in_kb} KB"