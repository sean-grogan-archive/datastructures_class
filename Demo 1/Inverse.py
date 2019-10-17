def main():
    liste = [10**0,10**1,10**2,10**3,10**4,10**5]
    print(liste)
    i_liste = inverse(liste)
    print(i_liste)
    
def inverse(element):
    inv = []
    for i in range(len(element)-1,-1, -1):
        inv.append(element[i])

    return inv

main()
