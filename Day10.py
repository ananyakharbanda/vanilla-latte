
def odd_numbers(n):
    list1 = []
    for x in range(n):
        if x % 2 == 1:
            list1.append(x)
    return list1

if __name__ == '__main__':

    y = odd_numbers(10)
    print(y)

    
