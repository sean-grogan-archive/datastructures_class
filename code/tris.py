import random
import time

"""Programme pour le cours IFT2015
   Écrit par François Major le 2 février 2014.
"""

"""Fonction principale"""
def main():

    # Lire en input un entier pour nombre d'éléments à trier
    n = int( input( "Entrez le nombre d'éléments à trier : " ) )

    dataBuffer = []
    for i in range( n ):
        dataBuffer.append( random.randint( 0, n-1 ) )

    data = dataBuffer.copy()
    avant = time.time()
    triMediane( data, 0, len(data)-1 )
    apres = time.time()
    print( "triMediane   :", apres-avant, "sec" )

    data = dataBuffer.copy()
    avant = time.time()
    triRapide( data, 0, len(data)-1 )
    apres = time.time()
    print( "triRapide    :", apres-avant, "sec" )

    data = dataBuffer.copy()
    avant = time.time()
    triSelection( data, len(data) )
    apres = time.time()
    print( "triSelection :", apres-avant, "sec" )

    data = dataBuffer.copy()
    avant = time.time()
    triInsertion( data, 0, len(data)-1 )
    apres = time.time()
    print( "triInsertion :", apres-avant, "sec" )

    data = dataBuffer.copy()
    avant = time.time()
    triMonceau( data )
    apres = time.time()
    print( "triMonceau   :", apres-avant, "sec" )

    data = dataBuffer.copy()
    avant = time.time()
    triComptage( data, n, n )
    apres = time.time()
    print( "triComptage  :", apres-avant, "sec" )

    data = dataBuffer.copy()
    avant = time.time()
    triSeaux( data, n )
    apres = time.time()
    print( "triSeaux     :", apres-avant, "sec" )

    data = dataBuffer.copy()
    avant = time.time()
    data.sort()
    apres = time.time()
    print( "Python sort  :", apres-avant, "sec" )

""" En temps linéaire, sépare tab[gauche, droite] autour du
    pivot = tab[indexPivot]. Le pivot se retrouve stocké à
    l'index pivpos, retourné par la fonction et tel que
    tab[gauche, pivpos] <= pivot et tab[pivpos+1, droite] > pivot.
"""
def partition( tab, gauche, droite, indexPivot ):
    pivot = tab[indexPivot]

    # déplacer le pivot à la fin du tableau
    swap( tab, indexPivot, droite )

    # toutes les valeurs <= pivot sont déplacées au début du tableau et
    # le pivot est inséré juste après elles.
    pivpos = gauche
    for i in range( gauche, droite ):
        if tab[i] <= pivot:
            swap( tab, pivpos, i )
            pivpos += 1
  
    swap( tab, pivpos, droite )
    return pivpos

""" Échange les valeurs aux indexes i et j
    de la liste tab
"""
def swap( tab, i, j ):
    tmp = tab[i]
    tab[i] = tab[j]
    tab[j] = tmp

"""En temps moyen linéaire, trouve la position du kième
   élément de tab, qui est modifié au fur et à mesure de
   l’exécution.
   Note 1 <= k <= droite-gauche+1. Pire cas quadratique, O(n^2).
"""
def selecteK( tab, k, gauche, droite ):
    i = random.randint( gauche, droite )
    indexPivot = partition( tab, gauche, droite, i )
    if ( gauche + k - 1 ) == indexPivot:
        return indexPivot

    # continuer la boucle, réduisant l’intervalle de manière appropriée.
    # Si on cherche dans la partition de gauche, alors on peut garder k.
    if ( gauche + k - 1) < indexPivot:
        return selecteK( tab, k, gauche, indexPivot-1 )
    else:
        return selecteK( tab, k - ( indexPivot - gauche + 1 ), indexPivot + 1, droite )

"""Trier le tableau tab[gauche, droite] utilisant la méthode de tri par la médiane.
"""
def triMediane( tab, gauche, droite ):

    # si la tranche du tableau à trier possède 1 (ou moins) éléments, c'est fini !
    if droite <= gauche:
        return

    # obtenir l'index du milieu du tableau
    # et la position de l’élément médiane
    # 1 <= k <= droite-gauche-1).
    milieu = (droite - gauche + 1)//2
    mediane = selecteK( tab, milieu, gauche, droite )

    triMediane( tab, gauche, gauche + milieu - 1 )
    triMediane( tab, gauche + milieu + 1, droite )


"""Trier le tableau tab[gauche..droite] avec la méthode de tri par insertion.
"""
def triInsertion( tab, gauche, droite ):
    for i in range( gauche, droite + 1 ):
        pos = i - 1
        valeur = tab[i]
        while pos >= 0 and tab[pos] > valeur:
            tab[pos+1] = tab[pos]
            pos -= 1
            tab[pos+1] = valeur

"""Trier le tableau tab[gauche..droite] avec la méthode de tri rapide.
"""
def triRapide( tab, gauche, droite):

  if droite <= gauche:
      return

  # partitions
  indexPivot = random.randint( gauche, droite )
  #indexPivot = gauche
  indexPivot = partition( tab, gauche, droite, indexPivot )

  triRapide( tab, gauche, indexPivot-1 )
  triRapide( tab, indexPivot+1, droite )

def selecteMax( tab, gauche, droite ):
    maxPos = gauche
    for i in range( gauche, droite+1 ):
        if( tab[i] > tab[maxPos] ):
            maxPos = i
    return maxPos

def triSelection( tab, n ):
    # répéter selecteMax et échanger avec l'endroit approprié
    for i in range( n-1, 0, -1 ):
        maxPos = selecteMax( tab, 0, i )
        if maxPos != i:
            swap( tab, i, maxPos )

def triMonceau( tab ):
    n = len( tab )
    construitMonceau( tab, n )
    for i in range( n-1, 0, -1 ):
        swap( tab, 0, i )
        monceaurise( tab, 0, i )

def construitMonceau( tab, n ):
    for i in range( n//2 - 1, -1, -1 ):
        monceaurise( tab, i, n )

def monceaurise( tab, i, max ):
    gauche = 2*i+1
    droite = gauche + 1
    if gauche < max and tab[gauche] > tab[i]:
        plusgrand = gauche
    else:
        plusgrand = i
    if droite < max and tab[droite] > tab[plusgrand]:
        plusgrand = droite
    if plusgrand != i:
        swap( tab, i, plusgrand )
        monceaurise( tab, plusgrand, max )

"""Trier n éléments dans tab qui sont dans l’intervalle 0 à k-1.
"""
def triComptage( tab, n, k):
    seau = []
    for i in range( k ):
        seau.append( 0 )

    for i in range( n ):
        seau[tab[i]] += 1

    idx = 0
    for i in range( k ):
        while seau[i] > 0:
            seau[i] -= 1
            tab[idx] = i
            idx += 1

def triSeaux( tab, n ):
    #création des seaux
    seau = []
    for i in range( n ):
        seau.append( [] )
    #création des partitions
    for i in range( n ):
        k = hash( tab[i] )
        seau[k].append( tab[i] )
    #extraction des données
    extraire( seau, tab, n )

def extraire( seau, tab, n ):
    idx = 0
    for i in range( n ):
        seau[i].sort()
        for m in range( 0, len(seau[i]) ):
            tab[idx] = seau[i][m]
            idx += 1

"""Appeler la fonction principale"""
main()
