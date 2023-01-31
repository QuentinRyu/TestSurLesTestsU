import unittest
from src.Methode import *
from datetime import datetime

class mainTest(unittest.TestCase):

    def test_Heure(self):
        date = datetime.now()
        heure = date.hour
        self.assertEqual(19,heure) 
    #mettre la valeur heure à jour pour faire le test

    def test_Salutation_Francais(self):
            date = datetime.now()
            heure = date.hour
            salutation = Saluer()

            if heure < 11 :
                return self.assertIn(Constantes.Francais.BONNE_MATINEE, salutation)
            elif heure <18 :
                return self.assertIn(Constantes.Francais.BONJOUR, salutation)
            else :
                return self.assertIn(Constantes.Francais.BONSOIR, salutation)

    def test_Salutation_Anglais(self):
            date = datetime.now()
            heure = date.hour
            salutation = Saluer()

            if heure < 11 :
                return self.assertIn(Constantes.Anglais.GOOD_MORNING, salutation)
            elif heure <18 :
                return self.assertIn(Constantes.Anglais.HELLO, salutation)
            else :
                return self.assertIn(Constantes.Anglais.GOOD_AFTERNOON, salutation)

        




if __name__ == "__main__":
    unittest.main()
