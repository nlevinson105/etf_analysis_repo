import pandas as pd
import requests
import time
import json

# portfolio_df_raw = pd.read_csv('etf_info_2.csv')


def get_expense_ratios(df):  # function to return list of expense ratios
    base_url = 'https://www.alphavantage.co/query?function=ETF_PROFILE&symbol='
    api_key = '&apikey=PO2AAG7Y6MDKW39M'
    exp_ratios = []

    for i in df['ticker']:
        link = f'{base_url}{i}{api_key}'
        a = requests.get(link)
        b = a.json()
        exp_ratio = float(b['net_expense_ratio'])
        exp_ratios.append(exp_ratio)

    return exp_ratios


# expense_ratios = get_expense_ratios(portfolio_df_raw)
# market_values = list(portfolio_df_raw['market_value'])


def get_annual_expense(exp, val):
    fund_annual_exp = [x * y for x, y in zip(val, exp)]
    total_annual_exp = sum(fund_annual_exp)

    total_exp_output = f'The annual expense of this portfolio is ${total_annual_exp: .2f}'
    return total_exp_output


def get_weighted_average_expense(exp, val):
    port_balance = sum(val)
    fund_weighted_exp = [(x / port_balance) * y for x, y in zip(val, exp)]
    total_weighted_exp = sum(fund_weighted_exp)

    total_weighted_exp_output = f'The weighted average expense ratio of this portfolio is {total_weighted_exp * 100}%'
    return total_weighted_exp_output


def expense_analysis(file):
    try:
        df = pd.read_csv(file)
        expense_ratios = get_expense_ratios(df)
        market_values = list(df['market_value'])
        annual_exp = get_annual_expense(expense_ratios, market_values)
        weighted_exp = get_weighted_average_expense(expense_ratios, market_values)
    except KeyError:
        print('Error: only valid ETF tickers accepted')
        annual_exp = None
        weighted_exp = None
    except TypeError:
        print('Error: market value must be a positive number')
        annual_exp = None
        weighted_exp = None
    except ValueError:
        print('Error: ticker and market value columns must be populated')
        annual_exp = None
        weighted_exp = None
    return annual_exp, weighted_exp


start_time = time.time()
print(expense_analysis('etf_info_2.csv'))
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

# correct answer is $33 and 0.165%











