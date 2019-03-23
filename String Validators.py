if __name__ == '__main__':
    s = input()
    # print(s.isalnum(), s.isalpha(), s.isdigit(), s.islower(), s.isupper(), sep='\n')
    for method in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']:
        print(any(eval("i." + method + "()") for i in s))
    # isalnum = isalpha = isdigit = islower = isupper = False
    # for i in s:
    #     if i.isalnum() == True:
    #         isalnum = True
    #     if i.isalpha() == True:
    #         isalpha = True
    #     if i.isdigit() == True:
    #         isdigit = True
    #     if i.islower() == True:
    #         islower = True
    #     if i.isupper() == True:
    #         isupper = True
    # print(isalnum, isalpha, isdigit, islower, isupper, sep='\n')
