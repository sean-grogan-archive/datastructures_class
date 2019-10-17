
import filecmp
from Mot import Mot

class Dictionnaire:
	
	def __init__(self):
		# TODO
		self._WordDict = dict()
		
	def __str__(self):
		# TODO
		#return str(self._WordDict)
		returned = []
		for i in self._WordDict:
			temp = (self._WordDict[i].get_cle(), self._WordDict[i].get_compte())
			returned.append(temp)

		return str(returned)


	def inserer(self, element):
		# TODO
		if self.trouver(element):
			self._WordDict[element].incrementer()
		else:
			self._WordDict[element] = Mot(element)
		
	def supprimer(self, element):
		# TODO
		if self.trouver(element):
			if self._WordDict[element].get_compte() == 1:
				del self._WordDict[element]
			else:
				self._WordDict[element].decrementer()
				
		
	def trouver(self, element):
		# TODO
		return element in self._WordDict #should return false if element 
	
	def get_mot(self, element):
		# TODO
		if element in self._WordDict:
			return self._WordDict[element]
		else:
			return None
		




if __name__ == '__main__':
	
	"""Validation de la classe (unit testing)"""
	
	liste = Dictionnaire()
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
		print("Une erreur s'est produite...(301)")
	elif not liste.trouver("to"):
		print("Une erreur s'est produite...(302)")
	elif liste.trouver("fragments"):
		print("Une erreur s'est produite...(303)")
	elif liste.trouver("qwerty"):
		print("Une erreur s'est produite...(304)")
	elif liste.get_mot("and").get_compte() != 6:
		print("Une erreur s'est produite...(305)")
	elif liste.get_mot("to").get_compte() != 1:
		print("Une erreur s'est produite...(306)")
	elif liste.get_mot("fragments") != None:
		print("Une erreur s'est produite...(307)")
		print(liste.get_mot("fragments"))
	elif liste.get_mot("qwerty") != None:
		print("Une erreur s'est produite...(308)")
	else:
		print("Auncun bug détecté.")










