#Fonctions importées

import random #fonction random dans le choix des phrases



#Liste game shifumi
shifumi = ["pierre", "papier", "ciseau"]

continuer = True
while continuer == True:

    user_input = input('\n ➜ ')

    bchoice= random.choice(shifumi)
    print()
    print(bchoice)
    print()

    if (user_input == bchoice):
        print("égalité... essaie encore ;)")
    elif (user_input == "pierre" and bchoice == "ciseau"):
        #cuddle = cuddle - 1
        print("Tu as gagné... Bidule ne voudra certainement plus jouer avec toi maintenant !")
    elif (user_input == "papier" and bchoice == "pierre"):
        #cuddle = cuddle - 1
        print("Tu as gagné... Bidule ne voudra certainement plus jouer avec toi maintenant !")
    elif (user_input == "ciseau" and bchoice == "papier"):
        #cuddle = cuddle - 1
        print("Tu as gagné... Bidule ne voudra certainement plus jouer avec toi maintenant !")
    else: 
        #cuddle = cuddle + 1
        print("Bidule t'a écrasé... tu peux aller pleurer !")

    choice = input ("\n Veux-tu continuer de jouer avec Bidule ? ")
    if choice == "oui": #and cuddle > 0:
        continuer = True
    else:
        continuer = False
        print("De toute façon, Bidule n'avait plus envie de jouer avec toi !") 

