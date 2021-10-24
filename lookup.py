
def lookup(a, b):
    list = []
    for i in a:
        for r in b:
            if i == r:
                list.append(i)
    return list

def freq(a):
    sum = 0
    already_checked = []
    for i in a:
        if i not in already_checked:
            already_checked.append(i)
            fmtstr = ''
            for r in a:
                if i == r:
                   sum = sum + 1
            timestr = 'time'
            if sum > 1:
                timestr = 'times'
            fmtstr = str(i) + ' occurs ' + str(sum) + ' ' + timestr
            sum = 0
            print(fmtstr)


if __name__ == '__main__':

    a = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 5, 5, 2, 2, 3, 9]
    b = [2, 5, 6, 7, 1]

    freq(a)
