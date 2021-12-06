
import math

if __name__ == '__main__':
    numparts = 1000000
    area = 0
    dx = 10 / numparts

    for i in range(numparts):
        area = area + (dx * math.pow(((i + 1) * dx + (i * dx))/2, 2))
    print(area)

