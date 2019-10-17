def main():
    liste1 = [10**0,10**1,10**2,10**3,10**4]
    liste2 = [10**0,10**1,10**2,10**3,10**1]

    print('liste1 is : ', liste1)
    print('is distinct?:', distincts(liste1))

    print('liste2 is : ', liste2)
    print('is distinct?:', distincts(liste2))
    
def distincts(element):
    for i in range(len(element)):
        for j in range(len(element)):
            if i != j:
                if element[i] == element[j]:
                    return False

    return True


main()
