import unittest
from services.heuristiikkafunktio import Heuristiikkafunktio as hf
from services.jps import JPS

class TestAlgoritmi(unittest.TestCase):
    def setUp(self):
        self.jps = JPS()
        self.matriisi1 = [[0,0,1,0,0],
                          [1,0,1,0,0],
                          [0,0,1,1,1],
                          [0,0,0,0,0],
                          [0,0,0,1,0]]
    
        self.matriisi2 = [[0,0,0,0,0,0],
                          [0,1,1,0,0,0],
                          [0,1,0,0,0,0],
                          [0,1,0,0,1,0],
                          [1,1,1,1,1,0],
                          [0,0,0,0,0,0]]

    def test_jps_paasee_paamaaraan_eika_palauta_nonea(self):
        palautus = self.jps.aloita((5,0), (0,5), self.matriisi2, h=hf.pythagoras)[1]
        self.assertIsNotNone(palautus)

    def test_jps_palauttaa_oikeat_koordinaatit(self):
        koordinaatit = self.jps.aloita((0,0), (4,4), self.matriisi1, h=hf.pythagoras)[0]
        self.assertEqual([(0,0), (1,1), (1,2), (2,3), (3,3), (4,4)], koordinaatit)
    
    def test_jps_palauttaa_none_kun_reittia_ei_loydy(self):
        palautus = self.jps.aloita((4,0), (0,4), self.matriisi1, h=hf.pythagoras)
        self.assertEqual(([], None, -1), palautus)