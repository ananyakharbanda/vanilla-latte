
def calc_marks(marks, regnum):
    a = 0
    for topic in marks:
        if regnum in marks[topic]:
            a = a + (marks[topic])[regnum]
    return a

if __name__ == '__main__':
    marks = {'algebra': {1: 20, 2: 21, 3: 22, 4: 25, 5: 27}, 'calculus': {1: 30, 2: 29, 3: 29, 4: 33, 5: 35}}
    print(calc_marks(marks, 2))
