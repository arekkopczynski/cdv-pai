from flask import Flask, render_template, url_for, request
from app import app, base

##tą zmienną będzie trzeba jakoś wpiąć do bazy danych
##pewnie trzeba by zrobic tak ze jedna tablica to jeden nowy wiersz w tabeli
data = []
for x in base.Expenses.query.all():
    data.append([x.id, x.name, x.value])

##tą zmienną będzie trzeba jakoś wpiąć do bazy danych
##a to izi bo to tylko jedna wartość musi być przechowana
money = 3240

warning = "Brak wystarczających środków do dodania wydatku"
warning2 = "Nie można dodać ujemnych pieniędzy?"
emptyWarning = " "

@app.route('/')
def index_base():
    return render_template('index_base.html', expenditures=data, money=money, warning=emptyWarning)


@app.route('/', methods=['POST'])
def my_money():
    global money
    global data

    if request.form['btn'] == 'Dodaj':
        moneey = request.form['money']
        if(int(moneey)<0):
            return render_template('index_base.html',expenditures=data, money=money, warning=warning2)
        else:
            money += int(moneey)
            return render_template('index_base.html',expenditures=data, money=money)
    elif request.form['btn'] == 'zatwierdź':
        expenditure = request.form['expenditure']
        cost = request.form['cost']
        if(int(cost)>money):
            return render_template('index_base.html',expenditures=data, money=money, warning=warning)
        else:
            data.append([expenditure, cost])
            money -= int(cost)
            return render_template('index_base.html',expenditures=data, money=money)
