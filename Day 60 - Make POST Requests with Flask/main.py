from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_data():
    
    login = {
        "name": request.form['username'],
        "password": request.form['password']
    }
    return render_template ("login.html", login=login)

if __name__ == '__main__':
    app.run(debug=True)