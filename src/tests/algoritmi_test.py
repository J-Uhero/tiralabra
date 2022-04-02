import unittest
from services.algoritmi import a_tahti

class TestAlgoritmi(unittest.TestCase):
    def setUp(self):
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
        """
        self.matriisi3 = [[0,0,0,0,0,0,0,0,0,0,0,0,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,0,0,1,0,0,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,0,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,1,0,1,0,1,0,1,0],
                          [0,1,0,1,0,0,0,0,0,0,0,1,0],
                          [0,1,0,1,1,1,1,1,1,1,0,1,0],
                          [0,1,0,0,0,0,0,0,0,0,0,1,0],
                          [0,1,1,1,1,1,1,1,1,1,1,1,0],
                          [0,1,0,0,0,0,0,0,0,0,0,0,0]]
        """

    def test_a_tahti_paasee_paamaaraan_eika_palauta_nonea(self):
        palautus = a_tahti((5,0), (0,5), m=self.matriisi2)
        self.assertIsNotNone(palautus)

    def test_a_tahti_palauttaa_oikeat_koordinaatit(self):
        koordinaatit = a_tahti((0,0), (4,4), m=self.matriisi1)
        self.assertEqual([(0,0), (1,1), (1,2), (2,3), (3,3), (4,4)], koordinaatit)
    
    def test_a_tahti_palauttaa_none_kun_reittia_ei_loydy(self):
        palautus = a_tahti((4,0), (0,4), m=self.matriisi1)
        self.assertEqual(None, palautus)

    """
    Tässä kokeilin erilaisten matriisien toimivuutta ja pääsenkö A*-algoritmin haaroihin

    def test_hakea_reitti_joka_kay_umpikujassa(self):
        palautus = a_tahti((0,27),(2,27), m=self.matriisi3)
        print(palautus)
        palautus2 = a_tahti((5,0), (0,5), m=self.matriisi2)
        #self.assertEqual(None, palautus)
    """
