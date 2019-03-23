if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        ls = input().strip().split()
        if ls[0] == 'insert':
            l.insert(int(ls[1]), int(ls[2]))
        elif ls[0] == 'print':
            print(l)
        elif ls[0] == 'remove':
            l.remove(int(ls[1]))
        elif ls[0] == 'append':
            l.append(int(ls[1]))
        elif ls[0] == 'sort':
            l.sort()
        elif ls[0] == 'pop':
            l.pop()
        elif ls[0] == 'reverse':
            l.reverse()
