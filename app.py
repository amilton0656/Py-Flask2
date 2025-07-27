from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def page_home():
    return render_template('home.html')

@app.route('/produtos')
def page_produto():
    return render_template('produtos.html')


