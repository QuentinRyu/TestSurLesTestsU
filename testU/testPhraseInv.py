import unittest
from src.Methode import PhraseInv


class testPhraseInv (unittest.TestCase):
    def test_PhraseInv(self):
        
        # QUAND on saisie une chaîne
        resultat = PhraseInv("toto")
        #ALORS celle-ci est renvoyé en miroir
        return self.assertEqual("otot", resultat)