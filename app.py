from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('inex.html')


@app.route("/about")
def about_me():
    return render_template('aboutMe.html')

@app.route("/BH")
def black_hole():
    return render_template('blackHole.html')

# @app.route("/")
# def home():
#     return "esta es la direccion /"

# @app.route("/")
# def home():
#     return "esta es la direccion /"

if __name__ == "__main__":
   app.run(debug=True) 