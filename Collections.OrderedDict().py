from collections import OrderedDict

if __name__ == '__main__':
    ordinary_dictionary = {}
    for _ in range(int(input())):
        ls = input().split()
        # print(' '.join(ls[:len(ls)-1]))
        # print(ls[len(ls)-1])
        if ' '.join(ls[:len(ls) - 1]) in ordinary_dictionary:
            ordinary_dictionary[' '.join(ls[:len(ls) - 1])] += int(ls[len(ls) - 1])
        else:
            ordinary_dictionary[' '.join(ls[:len(ls) - 1])] = int(ls[len(ls) - 1])
    # print(ordinary_dictionary)
    for name in ordinary_dictionary:
        print(name, ordinary_dictionary[name])
