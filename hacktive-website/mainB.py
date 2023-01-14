from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/about")
# def about():
#     return "about page"

@app.route("/loginstd")
def studlogin():
     return render_template("index2.html")

@app.route("/loginstaff")
def stafflogin():
     return render_template("index3.html")

@app.route("/stddetails")
def detailsstd():
     return render_template("index4.html")

@app.route("/staffdetails")
def detailsstaff():
     return render_template("index5.html")

@app.route('/reports/<path:path>')
def send_report(path):
    return render_template('reports', path)

if __name__=="__main__":
    app.run(debug=True)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)