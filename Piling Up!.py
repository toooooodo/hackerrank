def judge(list):
    # timeout
    # Max = max(list[0], list[len(list) - 1])
    # list.remove(Max)
    # while len(list) != 0:
    #     if max(list[0], list[len(list)-1]) > Max:
    #         print('No')
    #         return
    #     else:
    #         Max = max(list[0], list[len(list) - 1])
    #         list.remove(Max)
    # print('Yes')
    i = 0
    while i < len(list) - 1 and list[i] >= list[i + 1]:
        i += 1
    while i < len(list) - 1 and list[i] <= list[i + 1]:
        i += 1
    print('Yes' if i == len(list) - 1 else 'No')


if __name__ == '__main__':
    num = int(input())
    for i in range(num):
        n = int(input())
        # for j in range(n):
        #     list.append(int(input()))
        List = list(map(int, input().rstrip().split()))
        judge(List)
