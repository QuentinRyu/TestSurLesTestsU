import unittest
from ..src.Methode import *
from ..src.langues.Constantes import Constantes

class testPalindrome(unittest.TestCase):

    def testPalindromeAnglais(self):
        # QUAND on saisie une chaîne
        resultat = palindrome("kayak","kayak","eng")
        #ALORS celle-ci est renvoyé en miroir
        self.assertEqual(Constantes.Anglais.WELL_DONE, resultat)

    def testPalindromeFrancais(self):
        # QUAND on saisie une chaîne
        resultat = palindrome("kayak","kayak","fr")
        #ALORS celle-ci est renvoyé en miroir
        self.assertEqual(Constantes.Francais.BIEN_DIT, resultat)

    def test_PasPalindrome(self):
        # QUAND on saisie une chaîne
        resultat = palindrome("toto","otot")
        #ALORS celle-ci n'est pas renvoyée en miroir
        return self.assertEqual(":(", resultat)
