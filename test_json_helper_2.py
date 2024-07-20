import unittest
import pickle
import os

from json_helper_2 import read_json, read_dir_json, write_pickle

class testJsonHelper2(unittest.TestCase):


    def testReadJson(self):
            
        # given
        file_path = "data/super_smash_bros/pikachu.json"
        # when
        data = read_json(file_path)
        # then
        expected = {
        "name": "Pikachu",
        "neutral_special": "Thunderbolt",
        "side_special": "Quick Attack",
        "up_special": "Volt Tackle",
        "down_special": "Iron Tail",
        "final_smash": "Volt Tackle"
        }
        self.assertEqual(expected, data)

    def testReadAllJson(self):
        # given
        dir_path = "data/dragon_ball_z"
        # when
        data_objects = read_dir_json(dir_path)
        # then
        expected = [
            {
            "name": "Vegeta",
            "neutral_special": "Galick Gun",
            "side_special": "Final Flash",
            "up_special": "Jet Burn",
            "down_special": "Royal Guard",
            "final_smash": "Final Explosion"
            },
            {
            "name": "Goku",
            "neutral_special": "Kamehameha",
            "side_special": "Dragon Fist",
            "up_special": "Instant Transmission",
            "down_special": "Kaioken",
            "final_smash": "Super Spirit Bomb"
            }]
        self.assertEqual(expected, data_objects)

    def testWritePickle(self):
            #given
            # directory and expected pickle file path
            self.test_dir = 'data/super_smash_bros'
            self.pickle_file = os.path.join(self.test_dir, 'super_smash_characters.pickle')
        
            # when
            # read JSON files from directory
            data = read_dir_json(self.test_dir)
            # write data to pickle
            write_pickle(self.test_dir, data)
            
            # then
            # check pickle file was created
            self.assertTrue(os.path.exists(self.pickle_file))
            
            # assert contents of the pickle file
            with open(self.pickle_file, 'rb') as file:
                loaded_data = pickle.load(file)
                self.assertEqual(loaded_data, data)    
                