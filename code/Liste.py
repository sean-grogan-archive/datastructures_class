
import filecmp
from Mot import Mot

class Liste:
	
	def __init__(self):
		# TODO
	def __str__(self):
		# TODO
	def inserer(self, element):
		# TODO
	def supprimer(self, element):
		# TODO
	def trouver(self, element):
		# TODO
	def get_mot(self, element):
		# TODO




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
		print("Une erreur s'est produite...")
	elif not liste.trouver("to"):
		print("Une erreur s'est produite...")
	elif liste.trouver("fragments"):
		print("Une erreur s'est produite...")
	elif liste.trouver("qwerty"):
		print("Une erreur s'est produite...")
	elif liste.get_mot("and").get_compte() != 6:
		print("Une erreur s'est produite...")
	elif liste.get_mot("to").get_compte() != 1:
		print("Une erreur s'est produite...")
	elif liste.get_mot("fragments") != None:
		print("Une erreur s'est produite...")
	elif liste.get_mot("qwerty") != None:
		print("Une erreur s'est produite...")
	
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










