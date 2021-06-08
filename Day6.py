#determine velocity
def velocity(u, a, t):
    v = u + (a * t)
    print(v)

#determine displacement
def displacement(u, a, t):
    s = (u * t) + (1/2 * a * t * t)
    print(s)

def ladder(n):
    for i in range(n):
        row = ''
        for j in range(i+1):
            row = row + '* '
        print(row)

def rectangle(x, y):
    for i in range(x):
        row = ''
        for j in range(y):
            row = row + '* '
        print(row)


if __name__ == '__main__':

#determine velocity
    velocity(1, 2, 3)
#determine displacement
    displacement(5, 1, 2)

    rectangle(4, 5)
