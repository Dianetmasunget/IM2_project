from flask import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/palindromeresult',methods=["POST"])
def result():
    text = request.form["text"].lower()
    reversetext = text[::-1]

    if text == reversetext:
        msg = "The text is palindrome."
    else:
        msg = "The text  is not a palindrome."

    return render_template("pal.html",msg=msg)

@app.route('/divisible' ,methods=["POST"])
def divisible():
    number = int(request.form["number"])
    return render_template("div.html",number = number)



if __name__ == "__main__":
    app.run(debug=True)
