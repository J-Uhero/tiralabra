import unittest
from services.algoritmi import a_tahti

class TestAlgoritmi(unittest.TestCase):
    def setUp(self):
        self.matriisi1 = [[0,0,1,0,0],
                          [1,0,1,0,0],
                          [0,0,1,1,1],
                          [0,0,0,0,0],
                          [0,0,0,1,0]]
    
    def test_a_tahti_palauttaa_oikeat_koordinaatit(self):
        koordinaatit = a_tahti((0,0), (4,4), m=self.matriisi1)
        self.assertEqual([(0,0), (1,1), (1,2), (2,3), (3,3), (4,4)], koordinaatit)
    
    def test_a_tahti_palauttaa_none_kun_reittia_ei_loydy(self):
        palautus = a_tahti((4,0), (0,4), m=self.matriisi1)
        self.assertEqual(None, palautus)
