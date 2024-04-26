import pandas as pd
from sklearn.model_selection import train_test_split
from utils import load_config

def load_data(train_data_path, test_data_path):
    """
    Load training and testing data from CSV files.
    
    Args:
    train_data_path (str): Path to the training data CSV file.
    test_data_path (str): Path to the testing data CSV file.
    
    Returns:
    DataFrame, DataFrame: Training data, Testing data.
    """
    train_data = pd.read_csv(train_data_path)
    test_data = pd.read_csv(test_data_path)
    return train_data, test_data

def split_data(data, train_split, validation_split, test_split, shuffle=True):
    """
    Split data into training, validation, and testing sets.
    
    Args:
    data (DataFrame): The complete dataset.
    train_split (float): Proportion of the dataset to include in the train split.
    validation_split (float): Proportion of the dataset to include in the validation split.
    test_split (float): Proportion of the dataset to include in the test split.
    shuffle (bool): Whether to shuffle the data before splitting.
    
    Returns:
    DataFrame, DataFrame, DataFrame: Training data, Validation data, Testing data.
    """
    if not (train_split + validation_split + test_split) == 1:
        raise ValueError("The splits must sum to 1")

    train_data, temp_data = train_test_split(data, train_size=train_split, shuffle=shuffle)
    validation_data, test_data = train_test_split(temp_data, test_size=test_split / (validation_split + test_split), shuffle=shuffle)
    
    return train_data, validation_data, test_data

def prepare_data(config_path):
    """
    Prepare the data for training, validation, and testing based on the configuration.
    
    Args:
    config_path (str): Path to the configuration JSON file.
    
    Returns:
    DataFrame, DataFrame, DataFrame: Training data, Validation data, Testing data.
    """
    config = load_config(config_path)
    train_data_path = config['paths']['train_data_path']
    test_data_path = config['paths']['test_data_path']
    
    train_data, test_data = load_data(train_data_path, test_data_path)
    
    train_split = config['data_params']['train_split']
    validation_split = config['data_params']['validation_split']
    test_split = config['data_params']['test_split']
    shuffle = config['data_params']['shuffle']
    
    train_data, validation_data, test_data = split_data(train_data, train_split, validation_split, test_split, shuffle)
    
    return train_data, validation_data, test_data
