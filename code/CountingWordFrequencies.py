"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 23 mars 2014.
"""

def main():
    # Lire en input un nom de fichier
    filename = input( 'Entrez un fichier: ' )

    freq = {}
    for piece in open( filename ).read().lower().split():
    #only consider alphabetic characters
        print( "piece = ", piece )
        word = ''.join( c for c in piece if c.isalpha() )
        if word:
            print( "word = ", word )
            freq[word] = 1 + freq.get( word, 0 )

    max_word = ''
    max_count = 0

    for (w,c) in freq.items():
        if c > max_count:
            max_word = w
            max_count = c
    print( "The most frequent word is", max_word )
    print( "Its number of occurrences is", max_count )

"""Appeler la fonction principale"""
main()
