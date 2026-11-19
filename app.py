from flask import Flask, render_template, request
from fib4 import assess_fib4

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        try:
            age = float(request.form["age"])
            ast = float(request.form["ast"])
            alt = float(request.form["alt"])
            platelets = float(request.form["platelets"])
        except ValueError:
            error = "Please enter a number in every box."
        else:
            try:
                result = assess_fib4(age, ast, alt, platelets)
            except ValueError as problem:
                error = str(problem)

    return render_template("index.html", result=result, error=error)
