import winsound #I'm making an alarm!!
import random, time
from Mot import Mot
from Liste import Liste
from ListeTriee import ListeTriee
from Dictionnaire import Dictionnaire

# TODO


# MyWork Beg -------------------------------------
#RandSeed = random.randint(1,100)#picks a random Seed
RandSeed = 1
NumUnits = 1000
# main -------------------------------------------
def main():
	print('Sean Grogan\'s TP1') 
	print('ID# 20001636')
	 

# liste ------------------------------------------
def GenMotListe(Num):
	random.seed(RandSeed)
	MotListe = Liste()
	for i in range(Num):
		temp = Mot(None)
		insert = temp.get_cle()
		MotListe.inserer(insert)
	#print (MotListe) #Vis Test For Identity
	#deleting 5 random words
	d_beg = time.clock()
	for i in range(5):
		temp = Mot(None)
		gone = temp.get_cle()
		MotListe.supprimer(gone)
	d_end = time.clock()
	print('delete time     :',d_end - d_beg)
	



# listetriee -------------------------------------
def GenMotListeTriee(Num):
	random.seed(RandSeed)
	MotListe = ListeTriee()
	for i in range(Num):
		temp = Mot(None)
		insert = temp.get_cle()
		MotListe.inserer(insert)
	#print (MotListe) #Vis Test For Identity
	#deleting 5 random words
	d_beg = time.clock()
	for i in range(5):
		temp = Mot(None)
		gone = temp.get_cle()
		MotListe.supprimer(gone)
	d_end = time.clock()
	print('delete time     :',d_end - d_beg)
	

# dict -------------------------------------------
def GenMotDict(Num):
	random.seed(RandSeed)
	MotListe = Dictionnaire()
	for i in range(Num):
		temp = Mot(None)
		insert = temp.get_cle()
		MotListe.inserer(insert)
	#print (MotListe) #Vis Test For Identity
	#deleting 5 random words
	d_beg = time.clock()
	for i in range(5):
		temp = Mot(None)
		gone = temp.get_cle()
		MotListe.supprimer(gone)
	d_end = time.clock()
	print('delete time     :',d_end - d_beg)
	
# MyWork Fin -------------------------------------

# run --------------------------------------------
main()
print('Results: ')
print('Num Items   : ', NumUnits)
print('Random Seed : ', RandSeed)

print('Running \'Liste.py\'-------------------------------------------')
Liste_Beg = time.clock()
GenMotListe(NumUnits)
Liste_End = time.clock()
print('Liste Time      :',Liste_End-Liste_Beg)

print('Running \'ListeTriee.py\'--------------------------------------')
ListeT_Beg = time.clock()
GenMotListeTriee(NumUnits)
ListeT_End = time.clock()
print('ListeTriee Time :',ListeT_End-ListeT_Beg)

print('Running \'Dict.py\'--------------------------------------------')
Dict_Beg = time.clock()
GenMotDict(NumUnits)
Dict_End = time.clock()
print('Dict Time       :',Dict_End-Dict_Beg)


#file output::
filename = 'results_Outfile_'+str(NumUnits)+'_'+str(RandSeed)+'.csv'
with open(filename, 'w') as test:
		print('Results, ', file = test)
		print('Num Items,', NumUnits, file = test)
		print('Random Seed,', RandSeed, file = test)
		print('Liste Time,',Liste_End-Liste_Beg, file = test)
		print('ListeTriee Time,',ListeT_End-ListeT_Beg, file = test)
		print('Dict Time,',Dict_End-Dict_Beg, file = test)
		
winsound.Beep(400, 2500)#alarm for completion!
winsound.Beep(450, 2000)#alarm for completion!
winsound.Beep(400, 2500)#alarm for completion!
