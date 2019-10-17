def main():
	l = list() 
	while True:
		n = int(input ( "enter : "))
		if n == -1:
			break
		l.append (n)
		
def distincts(l):
	for i in l:
		if l.count(i) > 1:
			return False
	return True
	
	
main()