from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'gfhjmbjkvgdsfvds'

@app.route('/')
def index():
    return render_template("index.html")    

@app.route("/process", methods=["POST"])
def get_info():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/result")

@app.route('/result')
def result_render():
    return render_template("results.html")    

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')      
    
if __name__ == "__main__":
    app.run(debug=True)
