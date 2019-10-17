from TP3 import main

def fun_test(iteration, leprechauns):
    a = []
    for i in range(iteration):
        a.append(main(leprechauns))

    b = []
    for i in range(leprechauns+1):
        b.append(0)
    for i in a:
        for j in i:
            b[j] += 1

    return b
            
