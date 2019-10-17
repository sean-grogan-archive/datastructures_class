"""Programme pour le cours IFT2015
   Écrit par François Major le 11 janvier 2014.

   Ce programme prend en input une valeur entière
   et retourne en output la suite de Fibonacci
   jusqu'à cette valeur.
"""

"""Fonction principale"""
def main():
    # Lire en input un entier
    n = int( input( 'Entrez un entier positif: ' ) )

    """La fonction fibonacci retourne un générateur
       des nombres de la suite jusqu'à l'infini.
    """

    s = "["
    for fibo in fibonacci():
        if fibo > n:
            break
        s += str( fibo ) + ", "
    s += "... ]"
    print( s )

    """Accéder le kè élément de la suite"""
    # Lire en input un entier
    n = int( input( 'Entrez un entier positif: ' ) )

    k = 1
    for fibo in fibonacci():
        if k == n:
            s = "[" + str( fibo ) + "]"
            break
        k += 1
    print( s )

"""Fonction fibonacci utilisant un generateur.
"""
def fibonacci( ):
    a = 0
    b = 1
    while True:
        yield a
        portee = a + b # Fibonacci calcule portée de lapins !
        a = b
        b = portee

"""Appeler la fonction principale"""
main()
