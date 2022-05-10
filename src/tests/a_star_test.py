import unittest
from services.a_star import A_star

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

    def test_a_tahti_paasee_paamaaraan_eika_palauta_nonea(self):
        palautus = self.a_star.aloita((5,0), (0,5), m=self.matriisi2)
        self.assertIsNotNone(palautus)

    def test_a_tahti_palauttaa_oikeat_koordinaatit(self):
        koordinaatit = self.a_star.aloita((0,0), (4,4), m=self.matriisi1)[0]
        self.assertEqual([(0,0), (1,1), (1,2), (2,3), (3,3), (4,4)], koordinaatit)
    
    def test_a_tahti_palauttaa_none_kun_reittia_ei_loydy(self):
        palautus = self.a_star.aloita((4,0), (0,4), m=self.matriisi1)
        self.assertEqual(None, palautus)
