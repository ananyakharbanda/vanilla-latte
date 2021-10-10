
def min(list_num):
    min_num = 100000000000
    for a in list_num:
        if a < min_num:
            min_num = a
    return min_num

if __name__ == '__main__':

    numbers = [3, 4, 5, 2, 9]
    print(min(numbers))