from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/agendamento')
def agendamento():
    return render_template('agendamento.html')

@app.route('/descarte')
def descarte():
    return render_template('descarte.html')




if __name__ == '__main__':
    app.run(debug=True)
