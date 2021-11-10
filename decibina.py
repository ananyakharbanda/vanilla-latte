def lst2str(l):
    string = ''
    for i in l:
        string = string + str(i)
    print(string)

def deci2bina(n):
    l = []
    while n > 0:
        d = n % 2
        l.append(d)
        n = n // 2
    l.reverse()
    return lst2str(l)


if __name__ == '__main__':

    deci2bina()