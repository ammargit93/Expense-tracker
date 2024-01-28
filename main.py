from flask import Flask, render_template, request, redirect
import matplotlib.pyplot as plt
from datetime import datetime
from io import BytesIO
from helper import *
import base64
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'submit' in request.form:
            print('submit clicked')
            expense_name = request.form.get('expenseName')
            amount = request.form.get('amount')
            date = request.form.get('date')
            category = request.form.get('category')

            h = {"expenses": expense_name, "amount": amount, "date": date, "category": category}

            with open('data.json') as f:
                data = json.load(f)
            data['expense_data'].append(h)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=2)

        elif 'post' in request.form:
            return redirect('/submit')

    return render_template('expenses.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    arr = get_data()
    x, y = arr[1], arr[0]
    x = process_date(x)
    y = process_amount(y)
    plt.figure(figsize=(6, 4), dpi=200)

    plt.grid(True)
    plt.plot(x, y, marker='o')
    month = datetime.now().strftime('%b')
    plt.xlabel(f'Days in {month}')
    plt.ylabel('Total expense (INR)')
    plt.title('Daily Expenses')
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return render_template('plot.html', plot_url=plot_url)


if __name__ == '__main__':
    app.run(debug=True)
