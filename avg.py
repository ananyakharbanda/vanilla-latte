
def avg(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    count = len(numbers)
    average = sum / count
    return average

if __name__ == '__main__':

    numbers = [1, 2, 3, 4, 5, 6]
    print(avg(numbers))