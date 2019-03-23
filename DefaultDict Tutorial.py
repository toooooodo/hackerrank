from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    d = defaultdict(list)
    for i in range(n):
        x = input()
        d[x].append(str(i + 1))
    for _ in range(m):
        x = input()
        if x in d:
            print(' '.join(d[x]))
        else:
            print('-1')
        # print(d[x])
