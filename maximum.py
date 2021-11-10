# Revenue maximisation.
# A smartphone manufacturer Orange can sell 100 phones per month at $500 each.
# However, it can sell 20 additional units for each $10 reduction in price.
# Maximise the revenue.

if __name__ == '__main__':
    revenue = 0
    phones = 100
    cost = 500
    for i in range(100):
        y = (phones + (i * 20)) * (cost - (i * 10))
        if y > revenue:
            revenue = y
            nphones = phones + (i * 20)
            ncost = cost - (i * 10)
        else:
            break
    print(i)
    print('The maximum revenue that can be generated is $' + str(revenue) + ' which can be obtained by selling ' + str(nphones) + ' phones at $' + str(ncost) + ' each.' )