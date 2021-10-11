
def name(firstname, surname):
    final = []
    for i in range(len(firstname)):
        a = firstname[i]
        b = surname[i]
        final.append(a + ' ' + b)
    return final


if __name__ == '__main__':
    firstname = ['ananya', 'paras', 'neha']
    lastname = ['kharbanda', 'kharbanda', 'malik']
    print(name(firstname, lastname))