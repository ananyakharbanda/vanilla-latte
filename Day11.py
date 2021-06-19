
import math

def sine_function(a):
    list1 = []
    for x in a:
        b = math.sin(x)
        list1.append(b)
    return list1

#write a function that takes a list of arguments that are angles in radians; return list containing sine of angles
if __name__ == '__main__':

   x = sine_function([1, 2, 3.14, 4, 5, 6.28])
   print(x)