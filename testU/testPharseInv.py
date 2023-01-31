import unittest
from Projet import *
from src.Methode import *

class testPhraseInv (unittest.TestCase):
    def test_PhraseInv(self):
        
        # QUAND on saisie une chaîne
        resultat = PhraseInv("toto")
        #ALORS celle-ci est renvoyé en miroir
        return self.assertEqual("otot", resultat)