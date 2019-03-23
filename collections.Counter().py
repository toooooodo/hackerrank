from collections import Counter

if __name__ == '__main__':
    sum = 0
    input()
    shoes = Counter(list(map(int, input().rstrip().split())))
    x = int(input())
    for i in range(x):
        shoe, price = map(int, input().rstrip().split())
        if shoes[shoe] != 0:
            sum += price
            shoes[shoe] -= 1
    print(sum)
