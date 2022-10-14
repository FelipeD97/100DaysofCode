from flask import Flask, render_template

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        string = function()
        return f"<b>{string}<b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        string = function()
        return f"<em>{string}<em>"
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        string = function()
        return f"<u>{string}<u>"
    return wrapper_function


@app.route('/')
def hello_world():
    return "\
        <h1 style='text-align: center'>Hello, World!<h1>\
        <h3>It's my world<h3>\
        <img src='https://media3.giphy.com/media/ZfrYmoAdVhaXC/giphy.gif?cid=ecf05e47tb9prx9mjbbrzm31ghtmbuta6ckrqqbxo3bj4ldf&rid=giphy.gif&ct=g' width=200px /> "


@app.route('/<name>')
def my_name(name):
    # name = input("What is your name: ")
    return f'Your name is {name}'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye"


if (__name__) == '__main__':
    app.run(debug=True)
