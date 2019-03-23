def mutate_string(string, position, character):
    # ls = list(string)
    # ls[position] = character
    # return ''.join(ls)
    return string[:position] + character + string[position + 1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
