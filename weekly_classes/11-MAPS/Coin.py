"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 23 mars 2014.
"""

import random

class Coin:

    def flip( self ):
        return random.randint( 0, 1 ) == 0

"""unit testing
"""
if __name__ == '__main__':

    print( "Coin unit testing..." )

    coin = Coin()
    for i in range( 0, 10 ):
        print( coin.flip() )

    print( "end unit testing..." )
