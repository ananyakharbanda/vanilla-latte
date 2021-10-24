
def leapyear(a):
    ans = []
    for i in a:
        ret = isleapyear(i)
        if ret:
            ans.append(i)
    return ans

def isleapyear(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

if __name__ == '__main__':

    a = [100, 16, 400, 25, 2000, 2025]
    y = leapyear(a)
    print(y)