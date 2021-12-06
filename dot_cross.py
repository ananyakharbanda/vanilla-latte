
def dotproduct(vector1, vector2):
    product = 0
    for i in range(len(vector1)):
        product = product + (vector1[i] * vector2[i])
    return product

def crossproduct(vector1, vector2):
    pass

def stars1(n):
    stars = ''
    for i in range(n):
        stars = stars + '* '
        print(stars)

def stars2(n):
    stars = ''
    for i in range(n):
        stars = ((n - i) * ' ') + ((i + 1) * '*')
        print(stars)

def stars3(n):
    stars = ''
    for i in range(n):
        stars = (((n - i) // 2) * ' ') + ((i + 1) * ' *') + (((n - i) // 2) * ' ')
        print(stars)

if __name__ == '__main__':

    # stars1(5)
    # stars2(5)
    stars3(5)
    # vector1 = [1, 2, 3]
    # vector2 = [4, 5, 6]
    # print(dotproduct(vector1, vector2))

