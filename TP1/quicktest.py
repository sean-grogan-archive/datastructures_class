import filecmp

def main():
    print('tester')
    if filecmp.cmp("text1_Liste.txt", "text1_Liste_test.txt"):
        print('true')
    else:
        print('gah')
main()
