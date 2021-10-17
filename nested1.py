
def unvac(people):
    for i in people:
        if i[2] == False:
            print(i)

def printdigits(a):
    x = a // 100
    b = a - (100 * x)
    y = b // 10
    c = b - (10 * y)
    z = c // 1
    print(x, y, z)

def prigit(p):
    while p > 0:
        d = p % 10
        print(d)
        p = p // 10


if __name__ == '__main__':

    a = [['Stuti', 'Kansal', True], ['Ananya', 'Kharbanda', True], ['Navanshi', 'Pitliya', True], ['Manvay', 'Piltiya', False]]

    #unvac(a)

    #printdigits(756)

    prigit(756)
