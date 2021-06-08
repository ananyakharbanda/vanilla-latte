
def print_stars(count):
    for i in range(count):
        print('*')

def print_in_line(count):
    result = ''

    for i in range(count):
        result = result + '* '
        print (result)

    print (result)

def print_each_position(number):
    done = True

    #for i in range(100):
    while number  > 0:
        #if done:
            rem = number % 10
            #print(rem)
            number = number // 10
            #if number == 0:
            #   done = False

            print(rem)
            #print(number)

    #print ('4' + '5') (concatenation)

if __name__ == '__main__':
    print('ananya')


    print_stars(10)
    print ('finish')
    print_stars(3)

    print_in_line(10)

    name = 'ananya'
    lastname = 'kharbanda'

    if name == 'ananya' or lastname == 'malik':
        print ('bad')
    else:
        print ('good!')

    a = 10
    b = 2
    c = a // b

    d = a % b

    print (str(c) + ' R' + str(d))

    x = '10'
    y = '5.3'

    print(int(x) + float(y))

    #print
    #result
    #conditionals (if, elif, else)
    #data types (boolean(T/F), String, Number(integer and floating point)
    #loops (for (x) in range ..., division operator, remainder operator, integer --> string --> floating)

    #print('paras' + str(2))
    #print_each_position(12345)

    x = 10.1234
    strx = str(x)
    print(len(strx))

    xx = strx.split('.')
    #print(xx)
    print(xx[0])
    p = int(xx[1])

    print_each_position(p)





