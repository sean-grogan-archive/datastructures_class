"""Programme pour le cours IFT2015
   Écrit par François Major le 15 janvier 2014.

   Ce programme prend en input une valeur entière
   et retourne les nombres paires de la suite de
   Fibonacci en output jusqu'à cette valeur.
"""

"""Fonction principale"""
def main():
    # Lire en input un entier
    n = int( input( 'Entrez un entier positif: ' ) )

    """La fonction fibonacci retourne un générateur
       des nombres de la suite jusqu'à l'infini.
    """
    
    s = "["

    """La syntaxe de compréhension permet de produire
       4 types de contenant:

       [ k*k for k in range( 1, n+1 ) ] - liste
       { k*k for k in range( 1, n+1 ) } - ensemble
       ( k*k for k in range( 1, n+1 ) ) - générateur
       { k : k*k for k in range( 1, n+1 ) } - dictionnaire

       Dans le cas où on parcourt un générateur infini,
       on doit utiliser le générateur car si on utilise
       les 3 autres, alors python va vouloir compléter
       la liste, l'ensemble ou le dictionnaire pour la
       suite infinie.
    """
    for fibo in (f for f in fibonacci() if f % 2 == 0):
        if fibo > n:
            break
        s += str( fibo ) + ", "
    s += "... ]"
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
