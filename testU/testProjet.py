import unittest
from Projet import *
from src.Methode import *
from datetime import datetime

class mainTest(unittest.TestCase):

    def test_Heure(self):
        date = datetime.now()
        heure = date.hour
        self.assertEqual(19,heure) 
    #mettre la valeur heure à jour pour faire le test

    def test_Salutation(self):
            date = datetime.now()
            heure = date.hour
            salutation = Saluer()

            if heure < 11 :
                return self.assertEqual("Bonne matinée !", salutation)
            elif heure <18 :
                return self.assertEqual("Bonjour !", salutation)
            else :
                return self.assertEqual("Bonsoir !", salutation)


        




if __name__ == "__main__":
    unittest.main()
