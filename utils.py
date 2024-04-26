import json
import logging
import os

def load_config(config_path):
    """
    Load the configuration file.
    
    Args:
    config_path (str): Path to the configuration JSON file.
    
    Returns:
    dict: Configuration parameters.
    """
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config

def setup_logging(log_path, log_level):
    """
    Set up logging configuration.
    
    Args:
    log_path (str): Path to the log file.
    log_level (str): Logging level.
    """
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {log_level}')
    
    logging.basicConfig(filename=log_path, level=numeric_level,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

def ensure_dir(file_path):
    """
    Ensure that a directory exists.
    
    Args:
    file_path (str): Path to the directory.
    """
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

