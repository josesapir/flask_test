from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/operacional')
def operacional():
    return 'Operacional!'


@app.route('/soma/<a>/<b>')
def soma(a, b):
    return str(int(a)+int(b))


@app.route('/html')
def html():
    a = ['g','b','c','g']
    return render_template('h.html', a=a)


if __name__ == '__main__':
    app.run()