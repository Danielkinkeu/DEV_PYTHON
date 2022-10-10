

from random import randint

kdfd_const = 5
kdfd_inc = 0
print("***** le jeu du nombre mystere *****")
print(" le nombre mystere est compris entre 1 et 100 😎")
print("il te reste 05 essais")
kdfd_valeur = randint(1,100)
while(kdfd_inc != 5):
    print("devine le nombre : ")
    kdfd_entrer = input("_")
    if  kdfd_entrer.isdigit():
        kdfd_entrer = int(kdfd_entrer)
        kdfd_inc = kdfd_inc + 1
        kdfd_const = kdfd_const - 1 
        if kdfd_entrer == kdfd_valeur:
            print("bravo! le nombre mystere etait bien ", kdfd_entrer, "🙂")
            print("tu as trouver en ", kdfd_inc, "essais 🐱‍👤")
            print("fin de jeu")
        elif kdfd_entrer < kdfd_valeur:
            print("le nombre mystere est plus grand que ", kdfd_entrer,"😌🚀")
            if kdfd_const == 0:
                print("tu n'a plus d'essais! le nombre etait :_", kdfd_valeur)
                print("Fin du jeu")
            else:
                print("il te reste", kdfd_const,"essais")
        elif kdfd_entrer > kdfd_valeur:
            print("le nombre mystere est plus petit que ", kdfd_entrer,"😌🛬")
            if kdfd_const == 0:
                print("tu n'a plus d'essais! le nombre etait_ ", kdfd_valeur)
                print("Fin du jeu")
            else:
                print("il te reste", kdfd_const,"essais")
    else:
        print("veuillez entrer un nombre !")