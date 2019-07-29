from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    best = ["noodle", "ice cream", "matcha"]
    worst = ["artificial cherry", "powder sugar"]
    return render_template("index.html", fav=best, least_fav=worst, opposite_day=True)

if __name__ == '__main__':
   app.run(debug = True)
