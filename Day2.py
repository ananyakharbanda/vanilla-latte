interest_rate = 2/100


def new_balance(principal_amount, time):
    new_balance = (interest_rate * principal_amount * time) + principal_amount
    return new_balance

if __name__ == '__main__':

    paras_principal_amount = 1000

    paras_new_balance = new_balance(paras_principal_amount, 4)
    print (paras_new_balance)

    paras_new_balance = new_balance(paras_principal_amount, 4.5)
    print (paras_new_balance)
