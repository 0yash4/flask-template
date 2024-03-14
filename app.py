from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/EDA")
def about():
    return "<p>now we're in about say hi bitch</p>"


if __name__=="__main__":
    app.run(debug=True, port=8501)