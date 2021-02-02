proceeds = int(input('Type proceeds: '))
costs = int(input('Type costs: '))

if proceeds > costs:
    print('You are in profit! Congrats!')
    profitability = proceeds / costs
    print('Your profitability: ', profitability)
    employees = int(input('How many employees do you have? '))
    proceeds_per_employee = (proceeds - costs) / employees
    print('Your profit per employee: ', proceeds_per_employee)
elif proceeds < costs:
    print('You are lost profit, try better next time!')
