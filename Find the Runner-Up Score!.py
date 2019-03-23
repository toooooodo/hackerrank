if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort()
    i = len(arr) - 1
    while arr[i - 1] == arr[i]:
        i -= 1
    print(arr[i - 1])
