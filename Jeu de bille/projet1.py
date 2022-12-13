"""
Auteur : Jawad Cherkaoui
Date : 8 octobre 2022
But : Le jeu se joue avec des billes entre deux adversaires.
À partir d’un nombre initial de billes d ́exposées dans un sac
(le nombre initial est à convenir entre les deux joueurs),
chaque joueur retire à son tour 1, 2, 3 ou 4 bille(s).
Le joueur qui retire la dernière bille du sac perd la partie.
Entrée : variable --> graine, tot_billes, retire_billes
Sortie : tot_billes + les messages importés
"""

# Importation des modules : (messages, random, dont un nécessaire à "UpyLab")
from random import randint, seed
import messages                         # module important le ficher 'messages.py' pour utiliser ses variables
import sys
sys.path.append('/pub/code')

# Présentation du jeu :
print(messages.message_1)
graine = int(input(messages.entree_1))  # assignation de la variable graine
seed(graine)

# Règles :
print(messages.message_2)
tot_billes = int(input(messages.entree_2))  # assignation de la variable tot_billes
print(messages.message_3)                   # elle nous permet de connaitre le nombre actuel de bille
print(messages.message_4.format(tot_billes))
rejouer = str("oui")

while rejouer == str("oui"):  # boucle permettant de rejouer

    while tot_billes > 0:   # boucle ne mettant pas fin au jeu tant qu'il reste encore des billes

        # ----------------------------------------------- TOUR DU JOUEUR : nombre de billes retiré
        retire_billes = int(input(messages.entree_3))
        if retire_billes == 1 or 2 or 3 or 4:
            tot_billes = tot_billes - retire_billes

            if tot_billes == 1:
                print(messages.message_8)
                tot_billes = 0
            # -------------------------------------------- TOUR DE L'IA:
            elif (tot_billes - 1) % 5 == 0:
                print(messages.message_5.format(tot_billes))

                if tot_billes >= 7:
                    nbre_alea = randint(1, 100)            # création d'un nombre aléatoire grace au module 'random'

                    if nbre_alea <= 70:
                        print(messages.message_6)
                        print(messages.message_7.format(1))
                        tot_billes = tot_billes - 1                     # nouvelle valeur attribuer à la variable
                        print(messages.message_4.format(tot_billes))
                        if tot_billes == 1:                  # condition mettant fin au jeu s'il reste encore 1 bille
                            print(messages.message_9)
                            tot_billes = 0
                    else:
                        print(messages.message_6)
                        print(messages.message_7.format(2))
                        tot_billes = tot_billes - 2                     # nouvelle valeur attribuer à la variable
                        print(messages.message_4.format(tot_billes))
                        if tot_billes == 1:                 # condition mettant fin au jeu s'il reste encore 1 bille
                            print(messages.message_9)
                            tot_billes = 0
                else:
                    print(messages.message_6)
                    print(messages.message_7.format(1))
                    tot_billes = tot_billes - 1                         # nouvelle valeur attribuer à la variable
                    print(messages.message_4.format(tot_billes))
                    if tot_billes == 1:                 # condition mettant fin au jeu s'il reste encore 1 bille
                        print(messages.message_9)
                        tot_billes = 0

            else:
                print(messages.message_5.format(tot_billes))
                nbr = tot_billes
                while (tot_billes - 1) % 5 != 0:  # Boucle permettant de trouver un multiple de cinq
                    tot_billes = tot_billes - 1   # nouvelle valeur attribuer à la variable
                choix_logique = nbr - tot_billes  # nombre de billes à retirer
                print(messages.message_6)
                print(messages.message_7.format(choix_logique))
                if tot_billes != 1:
                    print(messages.message_4.format(tot_billes))
                elif tot_billes == 1:
                    print(messages.message_9)
                    tot_billes = 0

                                        # Fin de la partie
    rejouer = input(messages.entree_4)  # Demande au joueur s'il veut rejouer : oui / non
    if rejouer == str("oui"):
        print(messages.message_2)
        tot_billes = int(input(messages.entree_2))
        print(messages.message_3)
        print(messages.message_4.format(tot_billes))

    elif rejouer == str("non"):  # Fin de la boucle 'while' car fin du jeu
        print(end="")            # Arrêt du code
