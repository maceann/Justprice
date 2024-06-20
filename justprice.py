import random
#On va choisir un nombre au hasard
nombre_hasard = random.randint(1,100)
# on va demander au joueur d'entrer un nombre
nb_joueur = 0
# Si c'est plus petit que le nombre au hasard
while nb_joueur != nombre_hasard:
    nb_joueur = int(input("Entrer un nombre entre 1 et 100  "))

    if nb_joueur < nombre_hasard :
        print("C'est plus")
        #afficher "c'est plus"
   
    elif nb_joueur > nombre_hasard :
        print("C'est moins")
     #si c'est le même
    else :  
        nb_joueur = nombre_hasard 
        print ("Gagné")

    # afficher "Gagné"