kdfd_valeur = 0
kdfd_liste = []
kdfd_count = 0
kdfd_j = 0
while kdfd_valeur !=5 :
    print("choisissez parmi les 5 options suivantes :")
    print("1:   Ajouter un element a la liste")
    print("2:   Retirer un element de la liste")
    print("3:   Afficher la liste")
    print("4:   Vider la liste")
    print("5:   Quitter")
    kdfd_valeur = int(input("_ "))
    if kdfd_valeur == 1:
        kdfd_count = kdfd_count + 1
        print("🤖 votre choix :", kdfd_valeur)
        kdfd_list=str(input("entrez l'element a ajouter dans la liste: "))
        kdfd_liste.append(kdfd_list)
        print("l'element ",kdfd_list," a bien ete ajouter dans la liste 👌")
    elif kdfd_valeur == 2:
        print("🤖 votre choix :",kdfd_valeur)
        kdfd_list=str(input("entrez l'element a Suprimer dans la liste: "))
        for j in range(kdfd_count):
            if kdfd_liste[j] == kdfd_list:
                kdfd_j = 1
        if kdfd_j == 1:
            kdfd_liste.remove(kdfd_list)
            print("l'element ",kdfd_list," a bien ete retirer de la liste 👌")
        else:
            print("cet element ne se trouve pas dans la liste. veuillez revoir votre choix!")
    elif kdfd_valeur == 3:
        print("🤖 votre choix :",kdfd_valeur)
        print("voila votre liste ✔")
        for i in range(kdfd_count):
            print(i+1,"-",kdfd_liste[i])
    elif kdfd_valeur == 4:
        print("🤖 votre choix :",kdfd_valeur)
        kdfd_liste.clear()
        print("votre liste a bien ete vider 👌")
    elif kdfd_valeur == 5:
        print("🤖 votre choix :",kdfd_valeur)