from flask import Flask, jsonify, request, render_template


# Configure application
app = Flask(__name__)


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=["GET", "POST"])
def add_two_numbers():
    if 'param1' and 'param2' in request.args:
        num1 = request.args('param1')
        num2 = request.args('param2')
        return "Sum of {} and {} is {}".format(num1, num2, num1+num2)
    elif request.method == "POST":
        if not (request.form.get("param1") and request.form.get("param2")):
            return apology("Please enter two numbers to add", 400)

        num1 = request.form.get("param1")
        num2 = request.form.get("param2")

        render_template("added.html", param1=num1, param2=num2)

    else:
        return render_template('add.html')


@app.route('/subtract')
def subtract_two_numbers():
    pass
