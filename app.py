import os
from flask import Flask,render_template,request,session
from flask import redirect,url_for,flash

app=Flask(__name__)

@app.route("/")
def index():
    return "helloworld"

@app.route('/sample',methods=["GET"])
def sample():
    return render_template('sample.html')

@app.route('/login',methods=["Get","Post"])
def login():
    print(request.method)
    if request.method=="GET":
        return render_template("login.html")
    else:
        if request.form["email"]=="nazartvm@gmail.com" and request.form["password"]=="123456":
            session['loggedin']=True
            return redirect(url_for('home'));
        else:
            flash("fail")
            ##return redirect(url_for('login'))
    return redirect(url_for('login'))

@app.route('/home',methods=["Get"])
def home():
    return "home";


if __name__=="__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
