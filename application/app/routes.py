from flask import Flask, render_template, url_for, request
from app import app, base

warning = "Brak wystarczających środków do dodania wydatku"
warning2 = "Nie można dodać ujemnych pieniędzy?"
emptyWarning = " "

@app.route('/')
def index_base():

    #Get data from Database
    data = []
    for x in base.Expenses.query.all():
        data.append([x.name, x.value])

    return render_template('index_base.html', expenditures=data, money=base.total_funds(), warning=emptyWarning)

money=base.total_funds()
@app.route('/', methods=['POST'])
def my_money():
    global money

    #Get data from Database
    data = []
    for x in base.Expenses.query.all():
        data.append([x.name, x.value])

    if request.form['btn'] == 'Dodaj':
        moneey = request.form['money']

        if(int(moneey)<0):
            transaction = base.Incomes('', int(moneey))
            base.db.session.add(transaction)
            base.db.session.commit()
            base.db.session.remove()

            # No money to add but add button clicked
            return render_template('index_base.html',expenditures=data, money=base.total_funds(), warning=warning2)
        # Adding money to pocket
        else:

            transaction = base.Incomes('', int(moneey))
            base.db.session.add(transaction)
            base.db.session.commit()
            base.db.session.remove()

            money = base.total_funds()
            return render_template('index_base.html',expenditures=data, money=money)
    # Adding expenses
    elif request.form['btn'] == 'zatwierdź':
        expenditure = request.form['expenditure']
        cost = request.form['cost']
        if(int(cost)>int(money)):
            return render_template('index_base.html',expenditures=data, money=money, warning=warning)

        # Adding normal expenses
        else:
            # Add data to Database
            transaction = base.Expenses(expenditure, cost)
            base.db.session.add(transaction)
            base.db.session.commit()
            base.db.session.remove()

            #Get data from Database
            data = []
            for x in base.Expenses.query.all():
                data.append([x.name, x.value])

            money -= int(cost)
            return render_template('index_base.html',expenditures=data, money=money)
