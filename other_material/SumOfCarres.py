def main():
	n = int (input("n"))
	out = summe (n)
	
	print ( out )
	
def summe(n):
	total = sum (k*k for k in range (1,n+1))
	
	return total
	
main()
