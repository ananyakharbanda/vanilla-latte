
def sum_list(numbers):
    sum = 0
    for i in numbers:
        sum = i + sum
    return sum

def max(numbers):
    max_num = 0
    for a in numbers:
        if a > max_num:
            max_num = a
    return max_num

if __name__ == '__main__':

    numbers = [1, 82, 81, 96, 7]
    #print(sum_list(numbers))
    print(max(numbers))