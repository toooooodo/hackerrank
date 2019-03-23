from collections import Counter

if __name__ == '__main__':
    s = input()
    c = Counter(''.join(sorted(s)))
    for i in range(3):
        print(c.most_common(3)[i][0], c.most_common(3)[i][1])
