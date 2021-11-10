
def l2d(list):
    dictionary = {}
    for i in list:
        if i in dictionary:
            dictionary[i] = dictionary[i] + 1
        else:
            dictionary[i] = 1
    return dictionary

if __name__ == '__main__':
    print(l2d(list))