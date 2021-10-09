
def new_value(principal_value):
    list = []
    for i in principal_value:
        new_value = i + (0.1 * i)
        list.append(new_value)
    return list


if __name__ == '__main__':

    principal_value = [100, 120, 140]
    final = new_value(principal_value)
    print(final)