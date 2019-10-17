def main():
    v1 = [3,2,1]
    v2 = [-2,2,3,4]
    print(v1)
    print(v2)
    print(scalar(v1,v2))

def scalar(el1, el2):
    if len(el1) == len(el2):
        ret = []
        for i in range(len(el1)):
            ret.append(el1[i]*el2[i])

        return ret
    else:
        print ('error, unequal vector lengeths')
        return False
main()
