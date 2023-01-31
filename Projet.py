from src.Methode import *
from testU.testProjet import *
from testU.testPalindrome import *
def main():

    print(Saluer())

    phrase = str(input('dit quelque chose :'))
    print(phrase)

    phrase1 = PhraseInv(phrase)

    print (palindrome(phrase,phrase1))

    return Aurevoir()

main()