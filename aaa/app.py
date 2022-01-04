from flask import Flask, render_template, url_for, request


app = Flask(__name__)

data = (
        ('samochod', 1230),
        ('mieszkanie', 1990),
        ('jedzenie', 600),
    )

@app.route('/')
def index_base():
    return render_template('index_base.html', expenditures=data)



@app.route('/indexx', methods=['GET','POST'])
def indexx():
    if request.method == 'GET':
        return render_template('indexx.html')
    else:
        pierwszy_input = 'tak'
        if 'pierwszy_input' in request.form:
            pierwszy_input = request.form['pierwszy_input']
        
        drugi = 100
        if 'drugi' in request.form:
            drugi = request.form['drugi']

        return render_template('index_result.html', kasa=pierwszy_input, drugie=drugi)



