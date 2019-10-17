"""Programme pour le cours IFT2015
   Écrit par François Major le 11 janvier 2014.

   Ce programme prend en input une valeur entière
   et retourne en output les facteurs de cette valeur.
"""

"""Fonction principale"""
def main():
    # Lire en input un entier
    n = int( input( 'Entrez un entier positif: ' ) )

    """La fonction facteurs retourne les facteurs
       dans une liste.
    """
    print( 'Les facteurs de', n, 'sont :', facteurs( n ) )


"""Fonction facteurs retourne dans une liste
   les facteurs d'un entier positif n.
"""
def facteurs( n ):
    resultats = [] # liste initialisée vide
    for k in range( 1, n + 1 ):
        if n % k == 0:
            resultats.append( k )
    return resultats

"""Appeler la fonction principale"""
main()
