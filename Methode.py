from datetime import datetime
def Saluer():
    date = datetime.now()
    heure = date.hour

    if heure < 11 :
        salutation = "Bonne matinée !"
    elif heure <18 :
        salutation = "Bonjour !"
    else :
        salutation = "Bonsoir !"

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

def palindrome (phrase, phraseInv):

    if phrase == phraseInv :
        felicitation = "Bien Dit !"
    else:
        felicitation = "Ce n'est pas un palindrome :("
    return felicitation
    
def Aurevoir():
    date = datetime.now()
    heure = date.hour

    if heure < 11 :
        print("Passez une bonne matinée !")
    elif heure <18 :
        print("Bonne journée !")
    else :
        print("Bonne soirée !")

    return
