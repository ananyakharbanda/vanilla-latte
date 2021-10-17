
def reverseprint(a):
    b = len(a)
    while b > 0:
        c = a[b-1]
        print(c)
        b = b - 1

def reverseusingfor(a):
    for i in range(len(a)):
        print(a[len(a)-i-1])

if __name__ == '__main__':

    b = [1, 2, 3, 4, 5, 6, 7]
    reverseusingfor(b)