
def gparule(gpalist):
    for i in gpalist:
        sum = 0
        for a in range(2,len(i)):
            r = i[a]
            if r >= 80:
                sum = sum + 4.0
            elif r >= 70:
                sum = sum + 3.6
            else:
                sum = sum +3.2
        avg = sum/6
        print(avg)

if __name__ == '__main__':

    list1 = [['ananya', 2, 79, 80, 81, 82, 83, 84], ['vartika', 9, 75, 81, 82, 85, 70, 68]]

    gparule(list1)

