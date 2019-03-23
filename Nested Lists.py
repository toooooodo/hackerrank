if __name__ == '__main__':
    n = int(input())
    ls = [[input(), float(input())] for _ in range(n)]
    second_low = sorted(list(set([mks for name, mks in ls])))[1]
    print('\n'.join([a for a, b in sorted(ls) if b == second_low]))
