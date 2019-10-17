import time

def main():
	n = int(input("val n: "))
	m = int(input("val m: "))
	
	op = isMultiple(n,m)

	print (op)
	PAUSE()
	#time.sleep(5.5) 
	
def PAUSE():

	_wait = input("PRESS ENTER TO CONTINUE.")	
	
def isMultiple(n,m):
	if (n%m == 0):
			i = int(n/m)
			return i
	else:
			return False

main()
