from flask import Flask, render_template, url_for, request
from app import app, base

##tą zmienną będzie trzeba jakoś wpiąć do bazy danych
##a to izi bo to tylko jedna wartość musi być przechowana
money = 3240

warning = "Brak wystarczających środków do dodania wydatku"
warning2 = "Nie można dodać ujemnych pieniędzy?"
emptyWarning = " "

@app.route('/')
def index_base():

    #Get data from Database
    data = []
    for x in base.Expenses.query.all():
        data.append([x.name, x.value])

    return render_template('index_base.html', expenditures=data, money=money, warning=emptyWarning)


@app.route('/', methods=['POST'])
def my_money():
    global money

    #Get data from Database
    data = []
    for x in base.Expenses.query.all():
        data.append([x.name, x.value])

    if request.form['btn'] == 'Dodaj':
        moneey = request.form['money']

        # No money to add but add button clicked
        if(int(moneey)<0):
            return render_template('index_base.html',expenditures=data, money=money, warning=warning2)

        # Adding money to pocket
        else:
            money += int(moneey)
            return render_template('index_base.html',expenditures=data, money=money)
    # Adding expenses
    elif request.form['btn'] == 'zatwierdź':
        expenditure = request.form['expenditure']
        cost = request.form['cost']
        if(int(cost)>money):
            return render_template('index_base.html',expenditures=data, money=money, warning=warning)

        # Adding normal expenses
        else:
            # Add data to Database
            example_transaction = base.Expenses(expenditure, cost)
            base.db.session.add(example_transaction)
            base.db.session.commit()
            base.db.session.remove()

            #Get data from Database
            data = []
            for x in base.Expenses.query.all():
                data.append([x.name, x.value])

            money -= int(cost)
            return render_template('index_base.html',expenditures=data, money=money)
