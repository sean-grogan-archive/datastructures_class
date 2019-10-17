
import random

class Mot: 	#class Mot(object):

	def __init__(self, cle = None):
		# TODO
		#random.seed(5)
		cleBanque = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		if cle == None: #assigns a random key "cle" to the
				#Will generate a random word between 1 and 5 letters long
			WordLen = random.randint(1,5) #creates a random Word Length
			cle = ''
			for i in range(WordLen):
				cle += cleBanque[random.randint(0,25)]
			#print('word gen: ', cle)
			
		self._key = cle 
		self._tally = 1
		self._tups = (self._key,self._tally) 

	def __eq__(self, other):
		# TODO
		#print('eq called')
		return self._key == other 
	
	def __lt__(self, other):
		# TODO
		#print('lt called')
		return self._key < other._key
	
	def get_compte(self):
		# TODO
		return self._tally

	def get_cle(self):
		# TODO
		return self._key
	
	def incrementer(self):
		# TODO
		self._tally += 1
	
	def decrementer(self):
		# TODO
		self._tally -= 1


#testing a testor
if __name__ == '__main__':
	x=Mot('KEYTest')
	print('Cle:',x.get_cle())
	print('Compte:', x.get_compte())
	x.incrementer()
	print('Compte:', x.get_compte())
	x.incrementer()
	print('Compte:', x.get_compte())
	x.decrementer()
	print('Compte:', x.get_compte())
	x.decrementer()
	print('Compte:', x.get_compte())
	x.decrementer()
	print('Compte:', x.get_compte())
	print('Cle:',x.get_cle())
	print('test completed')
