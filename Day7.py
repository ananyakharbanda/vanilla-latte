
def print_list(list):
    for x in list:
        print(x)

def create_table(y):
    list1 = []
    for x in range(10):
        a = y * (x + 1)
        record = str(y) + ' x ' + str(x + 1) + ' = ' + str(a)
        list1.append(record)
    return list1

if __name__ == '__main__':

    t = create_table(5)

    print_list(t)