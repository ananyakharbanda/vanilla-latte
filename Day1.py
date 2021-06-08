cutoff_age_1 = 44
cutoff_age_2 = 18

def check_if_eligible(x):
    if x >= cutoff_age_1:
        print ('Ok, you can get vaccinated')
    elif x > cutoff_age_2:
        print('Wait, you cannot get vaccinated yet')
    else:
        print ('You are ineligible')

def add(x, y):
    result = x + y
    return result

def calculate_gpa(marks):
    if marks >= 80:
        return 4.0
    elif marks >= 70:
        return 3.6
    elif marks >= 60:
        return 3.2
    else:
        return ('FAIL!')

if __name__ == '__main__':

    papa_age = 44
    anan_age = 15
    mumma_age = 39

    check_if_eligible(papa_age)
    check_if_eligible(anan_age)
    check_if_eligible(mumma_age)

    answer = add(18, 22)

    print(answer)

    ananya_math = 84
    ananya_science = 80
    ananya_english = 50

    math_result = calculate_gpa(ananya_math)

    print(math_result)

    english_result = calculate_gpa(ananya_english)

    print(english_result)

    science_result = calculate_gpa(ananya_science)

    print(science_result)


