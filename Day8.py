
#sum of all the elements in a list
def sum_elements(input_list):
    sum = 0
    for x in input_list:
        sum = x + sum
    return sum

def print_list(list):
    for x in list:
        print(x)

#find out odd number
def odd_elements(input_list):
    result = []
    for a in input_list:
        if a % 2 != 0:
            result.append(a)
    return result

if __name__ == '__main__':

    list_a = [1, 45, 22, 67, 13, 24]

    x = odd_elements(list_a)
    print(x)

    add = sum_elements(x)
    print(add)