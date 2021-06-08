def table(n):
    for a in range(10):
        row = str(n) + ' x ' + str(a+1) + ' = ' + str(n * (a+1))
        print(row)

if __name__ == '__main__':

    table(77)
