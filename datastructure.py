
def sort(a):
    l = []
    min_num = 1000000000000
    while len(a) > 0:
        for i in a:
            if i < min_num:
                min_num = i
        a.remove(min_num)
        l.append(min_num)
        min_num = 1000000000000
    print(l)

def find_min(x):
    min = 1000000000000
    for r in x:
        if r < min:
            min = r
    return min

def sort2(x):
    list = []
    while len(x) > 0:
        min = find_min(x)
        list.append(min)
        x.remove(min)
    return list

if __name__ == '__main__':
    a = [11, 4, 9, 2, 5]
    #sort(a)
    y = sort2(a)
    print(y)