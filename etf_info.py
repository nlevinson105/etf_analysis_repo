import requests
import time
import json

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=ETF_PROFILE&symbol=QQQ&apikey=PO2AAG7Y6MDKW39M'
# r = requests.get(url)
# data = r.json()
# print(data)
# print(type(data))
#
# expense_ratio = float(data['net_expense_ratio'])
# print(expense_ratio)
# print(type(expense_ratio))

port_ids = [1, 2, 3]
port_tickers = ['VTI', 'QQQ', 'PFF']
port_balances = [10000, 6000, 4000]
# port_expenses = [0, 0, 0]
portfolio1 = {k: [v1, v2] for k, v1, v2 in zip(port_ids, port_tickers, port_balances)}
# print(portfolio1)


def expense_ratio_list(holdings):  # function to return list of expense ratios
    base_url = 'https://www.alphavantage.co/query?function=ETF_PROFILE&symbol='
    api_key = '&apikey=PO2AAG7Y6MDKW39M'
    exp_ratios = []

    for v1, v2 in holdings.values():
        link = f'{base_url}{v1}{api_key}'
        a = requests.get(link)
        b = a.json()
        exp_ratio = float(b['net_expense_ratio'])
        exp_ratios.append(exp_ratio)

    return exp_ratios


port_expenses = expense_ratio_list(portfolio1)
portfolio2 = {k: [v1, v2, v3] for k, v1, v2, v3 in zip(port_ids, port_tickers, port_balances, port_expenses)}
# print(portfolio2)


def annual_expense(holdings):  # function to return the total annual expense of a portfolio
    total_exp = 0

    for v1, v2, v3 in holdings.values():
        exp = v2 * v3
        total_exp += exp

    total_exp_output = f'The annual expense of this portfolio is ${total_exp: .2f}'
    return total_exp_output


def weighted_average_expense(holdings):  # function to the weighted average expense of a portfolio
    port_balance = 0
    total_weighted_exp = 0

    for v1, v2, v3 in holdings.values():
        port_balance += v2

    for v1, v2, v3 in holdings.values():
        weighted_exp = v3 * (v2 / port_balance)
        total_weighted_exp += weighted_exp

    total_weighted_exp_output = f'The weighted average expense ratio of this portfolio is {total_weighted_exp * 100}%'
    return total_weighted_exp_output


start_time = time.time()

print(annual_expense(portfolio2))
print(weighted_average_expense(portfolio2))

end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)


# correct answer is $33 and 0.165%







