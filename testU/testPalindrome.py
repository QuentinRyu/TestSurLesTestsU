import unittest
from Projet import *
from src.Methode import *

class testPalindrome(unittest.TestCase):

    def testPalindrome(self):
        # QUAND on saisie une chaîne
        resultat = palindrome("kayak","kayak")
        #ALORS celle-ci est renvoyé en miroir
        self.assertEqual("Bien Dit !", resultat)

    def test_PasPalindrome(self):
        # QUAND on saisie une chaîne
        resultat = palindrome("kayak","kayak")
        #ALORS celle-ci n'est pas renvoyée en miroir
        return self.assertEqual("Ce n'est pas un palindrome :(", resultat)
