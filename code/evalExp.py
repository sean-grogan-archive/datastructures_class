"""Programme pour le cours IFT2015
   Écrit par François Major le 15 février 2014.
   Adaptée de Matt Stallmann

   Ce programme prend en input une expression
   arithmétique et l'évalue
"""

from ArrayStack import ArrayStack
from ListStack  import ListStack

"""Fonction principale"""
def main():
    # Lire en input une expression
    expr = input( 'Entrez une expression: ' )
    print( "L'expression ", expr, "=", evalExp( expr ) )

"""Fonction parenMatch
"""
def evalExp( expr ):
    valStk = ArrayStack()
    opStk = ListStack()
    for z in expr:
        if z.isdigit():
            valStk.push( z )
        elif z in "+-*/":
            repeatOps( z, valStk, opStk )
            opStk.push( z )
    repeatOps( '$', valStk, opStk )
    return valStk.top()

def doOp( valStk, opStk ):
    x = valStk.pop()
    y = valStk.pop()
    op = opStk.pop()
    if op == '+':
        z = int(y) + int(x)
    elif op == '-':
        z = int(y) - int(x)
    elif op == '*':
        z = int(y) * int(x)
    elif op == "/":
        z = int(y) / int(x)
    valStk.push( z )

def prec( op ):
    if op in '*/':
        return 2
    elif op in "+-":
        return 1
    #this is '$'
    return 0

def repeatOps( refOp, valStk, opStk ):
    while len( valStk ) > 1 and prec( refOp ) <= prec( opStk.top() ):
        doOp( valStk, opStk )


"""Appeler la fonction principale"""
main()
