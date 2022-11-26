from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.answer import Dojo

@app.route('/')
def index():
    return render_template("index.html")    

@app.route("/process", methods=["POST"])
def get_info():
    if Dojo.is_valid(request.form):
        Dojo.save(request.form)
        return redirect("/result")
    return redirect("/")

@app.route('/result')
def result_render():
    return render_template("results.html", answer = Dojo.get_last_dojo())    


@app.route('/reset')
def go_back():
    return redirect("/")    

