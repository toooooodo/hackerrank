from collections import deque

if __name__ == '__main__':
    d = deque()
    x = int(input())
    for _ in range(x):
        ipt = input().split()
        if ipt[0] == 'append':
            d.append(ipt[1])
        elif ipt[0] == 'appendleft':
            d.appendleft(ipt[1])
        elif ipt[0] == 'pop':
            d.pop()
        else:
            d.popleft()
    print(' '.join(d))
