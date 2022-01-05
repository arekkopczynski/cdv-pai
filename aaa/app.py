from flask import Flask, render_template, url_for, request


app = Flask(__name__)

data = [
        ['samochod', 1230],
        ['mieszkanie', 1990],
        ['jedzenie', 600],
]


money = 3240 

@app.route('/')
def index_base():
    return render_template('index_base.html', expenditures=data, money=money)


@app.route('/', methods=['POST'])
def my_money():
    global money
    global data
    if request.form['btn'] == 'Dodaj':
        moneey = request.form['money']
        money += int(moneey)
        return render_template('index_base.html',expenditures=data, money=money)
    elif request.form['btn'] == 'zatwierdź':
        expenditure = request.form['expenditure']
        cost = request.form['cost']
        data.append([expenditure, cost])
        return render_template('index_base.html',expenditures=data, money=money)
        
    














