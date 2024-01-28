import numpy as np
import json


def get_data():
    amount_arr = np.array([])
    date_arr = np.array([])
    with open('data.json') as f:
        data = json.load(f)
    d = data['expense_data']
    for i in d:
        amount_arr = np.append(amount_arr, i['amount'])
        date_arr = np.append(date_arr, i['date'])
    return [amount_arr, date_arr]


def process_date(date):
    if date is not None:
        date_list = [str(d.split("-")[-1]) for d in date]
        return date_list
    return []


def process_amount(amount):
    if amount is not None:
        amt_list = [int(d.split("-")[-1]) for d in amount]
        return amt_list
    return []
