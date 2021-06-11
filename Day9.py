
#write a function named to_upper; will take a list of strings and return a list with all the strings in upper case

def to_upper(input_list):
    the_list = []
    for x in input_list:
        the_list.append(x.upper())
    return the_list

#add 2 lists

def add_lists(list1, list2):
    list = []
    a = len(list1)
    for i in range(a):
        z = list1[i] + list2[i]
        list.append(z)
    return list

if __name__ == '__main__':

    # x = ['AnaNYa', 'PaRaS', 'nEhA']
    # print(to_upper(x))

    list1 = [1, 3, 5, 7, 9, 11]
    list2 = [2, 4, 6, 8, 10, 12]
    print(add_lists(list1, list2))