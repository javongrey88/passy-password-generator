from flask import Flask, render_template, request
from password_generator import generate_password_hard

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        letters = int(request.form.get("letters"))
        symbols = int(request.form.get("symbols"))
        numbers = int(request.form.get("numbers"))
        password = generate_password_hard(letters, symbols, numbers)
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)