def main():
    liste = ['B','C','D','A','E','H','G','F']
    print(liste)
    insert = InsertSort(liste)
    print(insert)
    merge =  MergeSort(liste)
    print(merge)
    quick = inplace(liste, 0, len(liste) - 1)
    print(quick)
    
def InsertSort(element):
    for i in range(len(element)):
        j = i
        while((j > 0) & (element[j-1] > element[j])):
            element[j], element[j-1] = element[j-1], element[j]
            j = j - 1
    return element

def MergeSort(element):
    if len(element) <= 1:
        return element
    left = []
    right = []
    mid = len(element)//2
    for x in range(mid):
        left.append(element[x])
    for x in range(mid,len(element)):
        right.append(element[x])

    left = MergeSort(left)
    right = MergeSort(right)

    retlist = []
    for i in range(len(left)):
        retlist.append(left[i])
    for i in range(len(right)):
        retlist.append(right[i])
    
        
    return retlist
    
def inplace(S, a , b ):
    '''Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm.'''

    if a >= b: return # range is trivially sorted
    pivot = S[b] # last element of range is pivot
    left = a #will scan rightward
    right = b - 1 #will scan rightward
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right: # scans did not strictly cross
            S[left], S[right] = S[right], S[left] # swap values
            left, right = left + 1, right - 1# shrink range
        
    # put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    inplace(S, a, left - 1)
    inplace(S, left + 1, b)
     

main()
