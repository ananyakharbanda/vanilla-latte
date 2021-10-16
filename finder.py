
def finder(lon, a):
    for i in lon:
        if a == i:
            return True
    return False


def fre(lom, a):
    count = 0
    for i in lom:
        if a == i:
            count = count + 1
    return count


if __name__ == '__main__':

    lon = [1, 2, 2, 3, 4, 5, 6]
    a = 0

    print(fre(lon, a))
    print(finder(lon, a))