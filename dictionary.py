def update(diction, alist):
    for i in alist:
        if i in diction:
            diction[i] = diction[i] + 1
        else:
            diction[i] = 0
    return diction

if __name__ == '__main__':
    diction = {1: 2, 2: 4, 4: 8}
    list = [1, 8, 10]

    x = update(diction, list)
    print(x)
    

