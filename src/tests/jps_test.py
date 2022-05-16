import unittest
from math import sqrt
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
        
        self.matriisi3 = [[0,0,0,0,0,0],
                          [0,0,1,1,0,0],
                          [0,1,1,1,1,0],
                          [0,1,1,1,1,0],
                          [0,0,1,1,0,0],
                          [0,0,0,0,0,0]]

        self.matriisi4 = [[0,0,0,0,0,0],
                          [0,0,0,0,0,0],
                          [0,0,1,0,0,0],
                          [0,0,0,0,0,0],
                          [0,0,1,0,0,0],
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

    def test_jps_palauttaa_tyhjat_arvot_jos_koordineissa_on_este(self):
        palautus1 = self.jps.aloita((2,2), (0,0), self.matriisi3, h=hf.pythagoras)
        palautus2 = self.jps.aloita((0,0), (3,3), self.matriisi3, h=hf.pythagoras)
        self.assertEqual(([], None, -1), palautus1)
        self.assertEqual(([], None, -1), palautus2)

    def test_jps_loytaa_oikean_paatepisteen(self):
        reitti = self.jps.aloita((4,1), (1,4), self.matriisi3, h=hf.pythagoras)[0]
        self.assertEqual((1,4), reitti[-1])

    def test_jps_loytaa_oikean_pituisen_lyhimman_reitin(self):
        pituus = self.jps.aloita((4,1), (1,4), self.matriisi3, h=hf.pythagoras)[2]
        lyhin_reitti = 4*sqrt(2)+2
        self.assertAlmostEqual(lyhin_reitti, pituus)

    def test_jps_loytaa_jump_pointit(self):
        edeltajat = self.jps.aloita((0,5), (5,0), self.matriisi4, h=hf.pythagoras)[1]
        for jp in [(2,3), (3,2), (1,2), (2,5)]:
            self.assertIn(jp, edeltajat)

    def test_jps_antaa_saman_reitin_pituuden_molemmilla_heuristiikoilla(self):
        palautus1 = self.jps.aloita((0,0), (0,5), self.matriisi2, h=hf.pythagoras)[2]
        palautus2 = self.jps.aloita((0,0), (0,5), self.matriisi2, h=hf.esteeton)[2]
        self.assertEqual(palautus1, palautus2)

    def test_jps_sama_alku_ja_loppupiste(self):
        palautus = self.jps.aloita((0,0), (0,0), self.matriisi2, h=hf.pythagoras)
        self.assertEqual(palautus, ([(0,0)], {}, 0))

    def test_jps_paatepiste_yli_rajojen(self):
        palautus = self.jps.aloita((0,0), (6,0), self.matriisi2, h=hf.pythagoras)
        self.assertEqual(palautus, ([], None, -1))

    def test_jps_lahtopiste_yli_rajojen(self):
        palautus = self.jps.aloita((0,6), (0,0), self.matriisi2, h=hf.pythagoras)
        self.assertEqual(palautus, ([], None, -1))
