from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("pizza.html")

@app.route('/result',methods = ["post"])
def res():
    toppinglist = request.form.getlist("topping")
    if toppinglist:
        result = "You have a pizza with the toppings " + ", ".join(toppinglist[:-1])+ f", and {toppinglist[-1]}."
    else:
        result = "No toppings "
    return render_template("result.html",result = result)


if __name__ == "__main__":
    app.run(debug=True)