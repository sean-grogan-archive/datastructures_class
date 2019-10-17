"""Programme pour le cours IFT2015
   Écrit par Francois Major le 7 janvier 2014.

   Ce programme prend en input une valeur entière
   et retourne en output la factorielle de cette valeur.
"""

import time

"""Fonction principale"""
def main():
    # Lire en input un entier
    n = int( input( 'Entrez un entier positif: ' ) )

    """Calculer la factorielle de cet entier et
       sauvegarder le résultat dans une variable locale.
       On peut activer ou non la trace d'exécution de
       la fonction en 2è argument qui par défaut est False.
    """
    avant = time.time()
    fact = factorielle( n, False )
    apres = time.time()

    # Afficher le résultat
    print( 'La factorielle de', n, 'est', fact, 'calculée en', apres - avant, 'secondes' )

"""Fonction factorielle d'un entier positif n:

   n! = 1, si n = 0; n.(n-1).(n-2). ... 3.2.1 si n >= 1

   donne le nombre de permutations de n objets distincts.
   Par exemple, on peut permutter les trois caractères x, y et z
   de 3! = 3.2.1 = 6 manières différentes: xyz, xzy, yxz, yzx,
   zxy et zyx.

   La fonction possède une definition récursive naturelle, par
   exemple 13! = 13.12!, et n! = 1 si n = 0; n.(n-1)! si n >= 1.

   1! représente le cas de base qui n'est pas definit recursivement,
   (n-1)! représente le cas récursif.

   Trace d'exécution possible avec le 2è argument par défaut à False.
   La profondeur d'exécution est initialisée à 0 et on l'utilise
   pour indenter l'affichage de l'appel de la fonction.
"""
def factorielle( n, trace = False, profondeur = 0 ):
    if( trace ):
        print( profondeur * ' ','factorielle(', n, ')' )
    if n == 0:
        return 1
    else:
        return n * factorielle( n-1, trace, profondeur+1 )

"""La fonction n'utilise pas d'énoncé de boucle car la répétition
   est créée par des appels récursifs successifs. Il n'y a pas
   de circularité car chaque fois l'appel s'applique à un argument
   de plus en plus petit jusqu'au cas de base.
"""

"""Appeler la fonction principale"""
main()
