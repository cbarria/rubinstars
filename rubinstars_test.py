import unittest
from rubinstars import star_count
from github import Github
import yaml

class Teststar_count(unittest.TestCase):
	def test_input(self):
		#test if value is correct for 
		self.assertEqual(star_count("freeCodeCamp/freeCodeCamp"),yaml.dump({"freeCodeCamp/freeCodeCamp" : 345261})) #this value is dinamic =/
			
