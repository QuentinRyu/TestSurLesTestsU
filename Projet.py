from src.Methode import Saluer, PhraseInv, palindrome, Aurevoir

def main():

    print(Saluer("eng"))

    phrase = str(input('dit quelque chose :'))
    print(phrase)

    phrase1 = PhraseInv(phrase)

    print (palindrome(phrase,phrase1))

    return Aurevoir("eng")

main()