from datetime import datetime
from src.langues.Constantes import Constantes


def Saluer(langue):
        date = datetime.now()
        heure = date.hour

        if heure < 11 :
            if langue == "eng" :
                salutation = Constantes.Anglais.GOOD_MORNING
            else:
                salutation = Constantes.Francais.BONNE_MATINEE
        elif heure <18 :
            if langue == "eng" :
                salutation = Constantes.Anglais.HELLO
            else: 
                salutation = Constantes.Francais.BONJOUR
        else :
            if langue == "eng" :
                salutation = Constantes.Anglais.GOOD_AFTERNOON
            else :
                salutation = Constantes.Francais.BONSOIR

        return salutation

def PhraseInv(phrase):

        lst_phrase= []
        j = len(phrase)
        i = 0

        while i != j:
            
            lettre = phrase[j-1]
            lst_phrase.append(lettre)

            j = j - 1

        phrase = ''.join(lst_phrase)
        print(phrase)
        return phrase

def Palindrome (phrase, phraseInv, langue):

        if phrase == phraseInv :
            if langue == "eng" :
                resultat = Constantes.Anglais.WELL_DONE
            else :
                resultat = Constantes.Francais.BIEN_DIT
        else:
            resultat = ":("
        return resultat

def Aurevoir(langue):
        date = datetime.now()
        heure = date.hour

        if langue == "eng" :
            print(Constantes.Anglais.GOODBYE)

        else:
            print(Constantes.Francais.AU_REVOIR)
