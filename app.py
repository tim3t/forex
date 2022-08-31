from flask import Flask, render_template, redirect, request, session
from forex_python.converter import CurrencyRates

c = CurrencyRates(force_decimal=False)
CURRENT_AMOUNT_KEY = 'amount'

app = Flask(__name__)
app.config['SECRET_KEY'] = "lorb295ajke"

@app.route('/')
def redirect_to_converter_page():
    """Redirect to converter home page"""

    return redirect("/convertform")

@app.route('/convertform')
def convert_form_page():
    """Show conversion form"""

    return render_template("index.html")

@app.route('/convertform', methods=["POST"])
def handle_convert_form():
    """Form handling for conversion"""

    curr_fr = request.form["curr_fr"]
    curr_to = request.form["curr_to"]
    amount = request.form["amount"]
    converted = c.convert(f"{curr_fr}", f"{curr_to}", amount)
    converted = session[CURRENT_AMOUNT_KEY]
    return redirect("/conversion")

@app.route('/conversion')
def show_conversion():
    """Show conversion"""

    amount = session[CURRENT_AMOUNT_KEY]
    return render_template("result.html", amount = amount)
