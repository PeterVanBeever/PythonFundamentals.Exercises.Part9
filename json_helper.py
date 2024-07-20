import json
import os
import pickle

def read_json(file_path):
    """
    Given a string representing a file path to a json file, this function
    opens said file and converts its contents into a json object.
    
    Args:
    - file_path (str): The path to the json file.
    
    Returns:
    - dict: The contents of the json file as a dictionary.
    """
    with open(file_path, 'r') as file:
        json_object = json.load(file)
    return json_object

def read_all_json_files(directory_path: str):
    """
    Given a string representing a path to a directory, this function reads all
    of the json files in the directory and returns a list containing all of the
    json objects.
    
    Args:
    - directory_path (str): The path to the directory containing json files.
    
    Returns:
    - list: A list of dictionaries, each representing the contents of a json file.
    """
    json_objects = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
            json_objects.append(read_json(file_path))
    return json_objects

def write_pickle(file_path, data):
    """
    Given a file path and some data, this function writes the data to a file
    called super_smash_characters.pickle.
    
    Args:
    - file_path (str): The path where the pickle file will be saved.
    - data (any): The data to be pickled and saved.
    """
    pickle_file = os.path.join(file_path, 'super_smash_characters.pickle')
    with open(pickle_file, 'wb') as file:
        pickle.dump(data, file)

def load_pickle(file_path):
    """
    Given a file path, this function opens a pickled file and returns the data.
    
    Args:
    - file_path (str): The path to the pickle file.
    
    Returns:
    - any: The data loaded from the pickle file.
    """
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data
