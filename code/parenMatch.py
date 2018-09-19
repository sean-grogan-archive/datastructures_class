"""Programme pour le cours IFT2015
   Écrit par François Major le 15 février 2014.

   Ce programme prend en input une expression
   contenant des (), [] et {} et vérifie si ces
   symboles sont bien balancés
"""

from ArrayStack import ArrayStack
from ListStack  import ListStack

"""Fonction principale"""
def main():
    # Lire en input une expression
    expr = input( 'Entrez une expression: ' )
    print( "L'expression ", expr, "est balancée ?", parenMatch( expr ) )

"""Fonction parenMatch
"""
def parenMatch( expr ):
    aGauche = "({["
    aDroite = ")}]"
    S = ListStack()
    for c in expr:
        if c in aGauche:
            #si à symbole ouvrant, on empile
            S.push( c )
        elif c in aDroite:
            #si à symbole fermant...
            if S.is_empty():
                #si pile vide pas de match
                return False
            if aDroite.index( c ) != aGauche.index( S.pop() ):
                #si symbole fermant ne match pas symbole ouvrant
                return False
    #match si pile vide, sinon symbole(s) non matché(s)
    return S.is_empty()

"""Appeler la fonction principale"""
main()
