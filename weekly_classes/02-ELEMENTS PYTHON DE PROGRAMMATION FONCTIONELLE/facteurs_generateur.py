"""Programme pour le cours IFT2015
   Écrit par François Major le 11 janvier 2014.

   Ce programme prend en input une valeur entière
   et retourne en output les facteurs de cette valeur.
"""

"""Fonction principale"""
def main():
    # Lire en input un entier
    n = int( input( 'Entrez un entier positif: ' ) )

    """La fonction facteurs retourne un générateur
       des facteurs de n.
       Pour former un output de type liste, on utilise
       un iterateur.
    """

    s = []
    for f in facteurs( n ):
        s.append( f )

    # on veut les sortir triés
    s.sort()
    print( s )
    

"""Fonction facteurs utilisant un générateur.
   Explore les valeurs jusqu'à la racine carré de n.
"""
def facteurs( n ):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k  == n:
        yield k

"""Appeler la fonction principale"""
main()
