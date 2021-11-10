

if __name__ == '__main__':

    startu = 100
    startp = 500
    prevmaxrev = startp* startu
    for i in range(100):
        maxrev = (startp - ( i * 10))  * (startu + (i * 20))
        if maxrev >= prevmaxrev:
            print (str(startu + (i * 20)) + ' units at price ' + str(startp - ( i * 10)) + ' = ' + str(maxrev))
            prevmaxrev = maxrev
        else:
            print('finished after ' + str(i) + ' tries')
            break
