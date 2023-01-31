from Methode import *
from testProjet import *
def main():

    print(Saluer())

    phrase = str(input('dit quelque chose :'))
    print(phrase)

    phrase1 = PhraseInv(phrase)

    print (palindrome(phrase,phrase1))

    return Aurevoir()

main()