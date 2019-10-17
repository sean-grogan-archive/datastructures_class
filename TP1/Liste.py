
import filecmp
from Mot import Mot

class Liste:

	def __init__(self):
		# TODO
		self._WordList = []

	def __str__(self):
		# TODO
		returned = []
		for i in range(len(self._WordList)):
			temp = (self._WordList[i].get_cle(), self._WordList[i].get_compte())
			returned.append(temp)

		return str(returned)

	def inserer(self, element):
		# TODO
		#search for word in _WordList
		if Liste.trouver(self, element) == False:
			#print('element found: ', element)
			self._WordList.append(Mot(element))
		else:
			k = self.index_list(element)
			self._WordList[k].incrementer()
			#print('DUPLICATE found: ', self._WordList[k].get_cle(),',', self._WordList[k].get_compte())

	def supprimer(self, element):
		# TODO
		#print('Attempting to delete word: ', element)
		if Liste.trouver(self, element) == True:
			k = self.index_list(element)
			i = self._WordList[k].get_compte()
			if i > 1:
				#print('Decrementing....', self._WordList[k].get_compte())
				self._WordList[k].decrementer()
				#print('DECREMENTED!', self._WordList[k].get_compte())
			else:
				del self._WordList[k]
				#print('REMOVED!')
		#else:
			#print('Attempted to delete \'', element, '\'. No such Word')

	def trouver(self, element):
		# TODO
		#search for word in _WordList
		inList = False
		for i in range(len(self._WordList)):
			if element == self._WordList[i].get_cle():
				inList = True
				#print('Found in position: ',i)
				return True
				break
		if inList == False:
			return False

	def get_mot(self, element):
		# TODO
		if self.trouver(element) == True:
			k = self.index_list(element)
			return self._WordList[k]
		else:
			return None

	#my method to return the index of a point
	def index_list(self, element):
		# TODO
		#search for index
		inList = False
		for i in range(len(self._WordList)):
			if element == self._WordList[i]:
				#print('Found in position: ',i)
				inList = True
				return i
				break
		if inList == False:
			print('Erreur: illegal index_list')

## don't mess with this -------------------------------------------
if __name__ == '__main__':

	"""Validation de la classe (unit testing)"""

	liste = Liste()
	with open('text1.txt') as texte:
		for ligne in texte:
			liste_mots_ligne = ligne.split()
			for mot_brut in liste_mots_ligne:
				mot_strip = mot_brut.strip('!?%(),;:\'".')
				liste.inserer(mot_strip)

	liste.supprimer("and")
	liste.supprimer("to")
	liste.supprimer("fragments")
	liste.supprimer("qwerty")

	if not liste.trouver("and"):
		print("Une erreur s'est produite... (100)")
	elif not liste.trouver("to"):
		print("Une erreur s'est produite... (101)")
	elif liste.trouver("fragments"):
		print("Une erreur s'est produite... (102)")
	elif liste.trouver("qwerty"):
		print("Une erreur s'est produite... (103)")
	elif liste.get_mot("and").get_compte() != 6:
		print("Une erreur s'est produite... (104)")
	elif liste.get_mot("to").get_compte() != 1:
		print("Une erreur s'est produite... (105)")
	elif liste.get_mot("fragments") != None:
		print("Une erreur s'est produite... (106)")
	elif liste.get_mot("qwerty") != None:
		print("Une erreur s'est produite... (107)")
	
	with open('text1_Liste_test.txt', 'w') as test:
		print(liste, file = test)
	
	if filecmp.cmp("text1_Liste.txt", "text1_Liste_test.txt"):
		print("Aucun bug détecté.")
	else:
		print("Il y a un bug...")
		print("Alors que l'objet devrait s'imprimer ainsi :")
		print()
		print(open("text1_Liste.txt").read())
		print("Il s'imprime plutôt ainsi :")
		print()
		print(liste)










