
def print_name_email(people_database, to_find):
    for i in to_find:
        if i in people_database:
            a = people_database[i]
            for b in a:
                print(a[b])

if __name__ == '__main__':

    people_database = {'S1' : {'name' : 'Paras', 'email': 'pk@pk.com'}, 'S2': {'name' : 'Anan', 'email' : 'ak@ak.com'}}

    to_find = ['S1', 'S2']

    print_name_email(people_database, to_find)


