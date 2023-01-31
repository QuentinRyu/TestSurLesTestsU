import unittest
from Projet import *
from Methode import *
from datetime import datetime

class mainTest(unittest.TestCase):

    def test_PhraseInv(self):
        
        # QUAND on saisie une chaîne
        resultat = PhraseInv("kayak")
        #ALORS celle-ci est renvoyé en miroir
        return self.assertEqual("kayak", resultat)

    def test_Palindrome(self):
        # QUAND on saisie une chaîne
        resultat = palindrome("kayak","kayak")
        #ALORS celle-ci est renvoyé en miroir
        return self.assertEqual("Bien Dit !", resultat)

    def test_Heure(self):
        date = datetime.now()
        heure = date.hour

    #    return self.assertEqual(19,heure) 
    #enlever le commentaire du dessus et mettre la valeur heure à jour pour faire le test

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
