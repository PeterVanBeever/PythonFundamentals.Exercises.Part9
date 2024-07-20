import unittest
import os
import sys

# Add the directory containing json_helper.py to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/dragon_ball_z')))

from json_helper import read_json, read_all_json_files, write_pickle, load_pickle

class TestJsonHelper(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'data/marvel'
        self.test_dir2 ='data/super_smash_bros'
        self.test_json_file = os.path.join(self.test_dir2, 'mario.json')
        self.test_pickle_file = os.path.join(self.test_dir, 'super_smash_characters.pickle')

    def test_read_json(self):
        data = read_json(self.test_json_file)
        expected = {
            "name": "Mario",
            "neutral_special": "Fireball",
            "side_special": "Cape",
            "up_special": "Super Jump Punch",
            "down_special": "F.L.U.D.D.",
            "final_smash": "Mario Finale"
        }
        self.assertEqual(data, expected)

    def test_read_all_json_files(self):
        data = read_all_json_files(self.test_dir)
        expected = [
            {
            "name": "Iron Man",
            "neutral_special": "Repulsor Blast",
            "side_special": "Unibeam",
            "up_special": "Rocket Boost",
            "down_special": "Armor Lock",
            "final_smash": "Iron Legion"
            },
            {
            "name": "Doctor Strange",
            "neutral_special": "Mystic Arts",
            "side_special": "Portal Creation",
            "up_special": "Levitation",
            "down_special": "Mirror Dimension",
            "final_smash": "Infinity Gauntlet"
            },
            {
            "name": "Spider-Man",
            "neutral_special": "Web Shoot",
            "side_special": "Web Swing",
            "up_special": "Web Zip",
            "down_special": "Spider Sense",
            "final_smash": "Spider-Bots"
            }   
        ]
        self.assertEqual(data, expected)

if __name__ == '__main__':
    unittest.main()
