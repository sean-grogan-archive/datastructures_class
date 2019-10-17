"""Classe pour le cours IFT2015
   Écrit par Francois Major le 12 janvier 2014.

   Cette classe définit un morceau de musique
   qui possède les attributs suivants :
       - le numéro (sur l'album)
       - un nom
       - un artiste interprète
       - une durée (en secondes)
       - un tempo (en percussions par minute)
       - une année de parution
       - un genre
       - un nombre limite d'audition
"""

class morceau:

    """Constructeur
    """
    def __init__( self, numero, nom, artiste, duree, tempo, parution, genre, lim_audition = 3 ):

        self._numero       = numero
        self._nom          = nom
        self._artiste      = artiste
        self._duree        = duree
        self._tempo        = tempo
        self._parution     = parution
        self._genre        = genre
        self._lim_audition = lim_audition

        # Initialement, le morceau n'a pas été joué
        self._audition = 0

    """Les methodes
    """

    """__str__ retourne une chaîne lisible
    """
    def __str__( self ):
        s = "morceau( "
        s += str( self._numero ) + ", "
        s += str( self._nom ) + ", "
        s += str( self._artiste ) + ", "
        s += str( self._duree ) + ", "
        s += str( self._tempo ) + ", "
        s += str( self._parution ) + ", "
        s += str( self._genre ) + ", "
        s += str( self._audition ) + ", "
        s += str( self._lim_audition ) + " )"
        return s

    """Les fonctions get
    """

    def obtenir_numero( self ):
        return self._numero

    def obtenir_nom( self ):
        return self._nom

    def obtenir_artiste( self ):
        return self._artiste

    def obtenir_duree( self ):
        return self._duree

    def obtenir_tempo( self ):
        return self._tempo

    def obtenir_parution( self ):
        return self._parution

    def obtenir_genre( self ):
        return self._genre

    def obtenir_audition( self ):
        return self._audition

    def obtenir_lim_audition( self ):
        return self._lim_audition

    """joue si la lim_audition n'est pas atteinte.
       Retourne True si jouable; False autrement.
    """
    def jouer( self ):
        if self._audition < self._lim_audition:
            self._audition += 1
            return True
        else:
            return False

    """jouable si audition <= lim_audition
    """
    def jouable( self ):
        return self._audition < self._lim_audition

"""Fin class tune:
"""

"""Validation de la classe (unit testing)
"""

if __name__ == '__main__':

    morceauA = morceau( 1, 'Beast of Burden (Live)', 'The Rolling Stones', 307, 113, 2014, 'Rock' )
    morceauB = morceau( 1, 'Beast of Burden (Live)', 'The Rolling Stones', 307, 113, 2014, 'Rock', 4 )
    mesmorceaux = [morceauA, morceauB]

    for m in mesmorceaux:
        print( m )
        for i in range( 1, 5 ):
            if m.jouable():
                m.jouer()
                print( 'Écoute du morceau...' )
                if m.jouable():
                    print( 'Le morceau joue, et pourra être joué encore', m.obtenir_lim_audition() - m.obtenir_audition(), 'fois.' )
                else:
                    print( 'Le morceau joue pour la dernière fois.' )
            else:
                print( 'Le morceau ne peut plus jouer, il a déjà été joué', m.obtenir_audition(), 'fois.' )

"""Fin Validation de la classe (unit testing)
"""
