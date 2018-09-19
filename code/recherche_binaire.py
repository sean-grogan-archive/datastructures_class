"""Programme pour le cours IFT2015
   Écrit par François Major le 8 janvier 2014.

   Ce programme prend en input une valeur entière
   et la recherche dans une séquence indexable
   telle une liste en python
"""

"""Fonction principale"""
def main():

    data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]

    """Boucler en entrée du nombre entier à chercher
       dans les données jusqu'à ce que la valeur 0
       soit entrée par l'usager.
    """

    # Imprimer en output les data
    print( data )

    # Lire en input un entier
    element = int( input( 'Entrez un entier positif (0 pour terminer): ' ) )

    while element != 0:
        trouve = recherche_binaire( data, element, 0, len( data )-1, True )
        if trouve:
            print( "J'ai trouvé", element, 'dans data !' )
        else:
            print( "Je n'ai pas trouvé", element, 'dans data !' )

        # Lire l'entier suivant
        element = int( input( 'Entrez un entier positif (0 pour terminer): ' ) )


"""Fonction recherche binaire d'un élément cible dans une
   séquence de données implantée avec une liste. La liste,
   la cible, et les indices min et max qui bornent la recherche
   dans la séquence sont passés en arguments.

   La fonction retourne True si la cible est trouvee dans la liste.
"""
def recherche_binaire( data, cible, min, max, trace = False, profondeur = 0 ):
    print( profondeur * ' ', 'recherche_binaire(', data, ',', cible, ',', min, ',', max, ',', trace, ')', )
    if min > max:
        return False #interval vide, pas de match
    else:
        milieu = (min + max) // 2
        if cible == data[milieu]:
            return True
        elif cible < data[milieu]:
            #on cherche dans la portion gauche de la liste
            return recherche_binaire( data, cible, min, milieu-1, trace, profondeur+1 )
        else:
            #on cherche dans la portion droite de la liste
            return recherche_binaire( data, cible, milieu+1, max, trace, profondeur+1 )

"""Appeler la fonction principale"""
main()
