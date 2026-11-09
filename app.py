from flask import Flask 

app = Flask(__name__)

@app.route("/")
def home():
    return "esta es la direccion /"


@app.route("/about")
def about_me():
    return "aqui va sobre mi"

# @app.route("/")
# def home():
#     return "esta es la direccion /"

# @app.route("/")
# def home():
#     return "esta es la direccion /"

if __name__ == "__main__":
   app.run(debug=True) 