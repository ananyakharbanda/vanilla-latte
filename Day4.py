def is_leap_year(y):
    if y % 100 == 0:
        if y % 400 == 0:
            return True
        else:
            return False
    elif y % 4 == 0:
        return True
    else:
        return False



if __name__ == '__main__' :

    for a in range(100):
       if a % 3 == 0 and a != 0 or a % 5 == 0:
           print(a)

    first_names = ['ananya', 'paras', 'neha']
    last_names = ['kharbanda', 'kharbanda', 'malik']

    for i in range(3):
        if i > 1:
            full_name = first_names[i] + ' ' + last_names[i]
            print(full_name)

    answer = is_leap_year(3000)
    print(answer)

