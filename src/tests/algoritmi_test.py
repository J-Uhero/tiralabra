import unittest
from services.algoritmi import a_tahti

class TestAlgoritmi(unittest.TestCase):
    def setUp(self):
        self.matriisi1 = [[0,0,1,0,0],
                          [1,0,1,0,0],
                          [0,0,1,1,1],
                          [0,0,0,0,0],
                          [0,0,0,1,0]]
        
        self.matriisi2 = [[0,0,1,0,0],
                          [0,0,1,0,0],
                          [1,1,1,0,0],
                          [0,0,0,0,0],
                          [0,0,0,0,0]]
    
    def test_a_tahti_palauttaa_oikeat_koordinaatit(self):
        pass
