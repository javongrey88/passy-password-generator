from flask import Flask, render_template, request
from password_generator import generate_secure_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        try:
            nr_letters = int(request.form.get("letters"))
            nr_symbols = int(request.form.get("symbols"))
            nr_numbers = int(request.form.get("numbers"))
            password = generate_secure_password(nr_letters, nr_symbols, nr_numbers)
        except (ValueError, TypeError):
            password = "⚠️ Invalid input. Please enter numbers only."
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
