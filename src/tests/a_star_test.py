import unittest
from math import sqrt
from services.a_star import A_star
from services.heuristiikkafunktio import Heuristiikkafunktio as hf

class TestAlgoritmi(unittest.TestCase):
    def setUp(self):
        self.a_star = A_star()
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
        
        self.matriisi3 = [[0,0,0,0,0,0],
                          [0,0,1,1,0,0],
                          [0,1,1,1,1,0],
                          [0,1,1,1,1,0],
                          [0,0,1,1,0,0],
                          [0,0,0,0,0,0]]

    def test_a_tahti_paasee_paamaaraan_eika_palauta_nonea(self):
        palautus = self.a_star.aloita((5,0), (0,5), m=self.matriisi2, h=hf.pythagoras)
        self.assertIsNotNone(palautus)

    def test_a_tahti_palauttaa_oikeat_koordinaatit(self):
        koordinaatit = self.a_star.aloita((0,0), (4,4), m=self.matriisi1, h=hf.pythagoras)[0]
        self.assertEqual([(0,0), (1,1), (1,2), (2,3), (3,3), (4,4)], koordinaatit)
    
    def test_a_tahti_palauttaa_none_kun_reittia_ei_loydy(self):
        palautus = self.a_star.aloita((4,0), (0,4), m=self.matriisi1, h=hf.pythagoras)
        self.assertEqual(([], None, -1), palautus)
    
    def test_a_tahti_palauttaa_tyhjat_arvot_jos_koordineissa_on_este(self):
        palautus1 = self.a_star.aloita((2,2), (0,0), self.matriisi3, h=hf.pythagoras)
        palautus2 = self.a_star.aloita((0,0), (3,3), self.matriisi3, h=hf.pythagoras)
        self.assertEqual(([], None, -1), palautus1)
        self.assertEqual(([], None, -1), palautus2)

    def test_a_tahti_loytaa_oikean_paatepisteen(self):
        reitti = self.a_star.aloita((4,1), (1,4), self.matriisi3, h=hf.pythagoras)[0]
        self.assertEqual((1,4), reitti[-1])
    
    def test_a_tahti_loytaa_lyhyimman_pituisen_reitin(self):
        pituus = self.a_star.aloita((4,1), (1,4), self.matriisi3, h=hf.pythagoras)[2]
        lyhin_reitti = 4*sqrt(2)+2
        self.assertAlmostEqual(lyhin_reitti, pituus)
