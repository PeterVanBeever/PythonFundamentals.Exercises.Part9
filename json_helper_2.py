import json
import os
import sys
import pickle

# relative file paths
f_luigi = "data/super_smash_bros/luigi.json"  
f_zelda = "data/super_smash_bros/zelda.json"
d_marvel = "data/marvel"
d_dragbal = "data/dragon_ball_z"



# function to read json files
def read_json(file_path): 
    with open(file_path, 'r+') as jfile:
        jobject =  json.load(jfile)
        return jobject
    
        # given a string = file_path
        # open the json file
        # convert json file to json object
        # return json object

# function to read all json files in a directory
def read_dir_json(dir_path):
    # set json_data as a list to collect jsons
    json_objects = []
    # check directory
    for jfilename in os.listdir(dir_path):
        # for each file, check if json
        if jfilename.endswith('.json'):
            file_path = os.path.join(dir_path, jfilename)
            # if json, open file
            with open(file_path, 'r') as file: 
                data = json.load(file)
                # add 
                json_objects.append(data)
    return json_objects


# data/super_smash_bros
# function to write a pickle file
def write_pickle(file_path, data):
    # path to save supersmash
    pickle_file = os.path.join(file_path, 'super_smash_characters.pickle')
    with open(pickle_file,'wb') as file:
        pickle.dump(data, file)


# pickle_file = os.path.join(file_path, 'super_smash_characters.pickle')
#     with open(pickle_file, 'wb') as file:
#         pickle.dump(data, file)