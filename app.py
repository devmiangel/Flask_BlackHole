from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about_me():
    return  render_template('aboutMe.html')

@app.route("/black_hole")
def black_hole():
    return  render_template('blackHole.html')

@app.route("/black_hole/<int:bh_id>")
def black_hole_detail(bh_id):
    return  render_template(f'blackHoleDetail{bh_id}.html')

@app.route("/sources")
def sources():
    return  render_template('sources.html')

if __name__ == "__main__":
   app.run(debug=True) 