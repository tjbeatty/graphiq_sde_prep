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


def request_args():
    num1 = float(request.args['param1'])
    num2 = float(request.args['param2'])

    return [num1, num2]


def request_form_get():
    num1 = float(request.form.get("param1"))
    num2 = float(request.form.get("param2"))

    return [num1, num2]


def make_ints(num1, num2):
    if num1 % 1 == 0 and num2 % 1 == 0:
        num1 = int(num1)
        num2 = int(num2)

    return [num1, num2]


def api_params():
    [num1, num2] = request_args()
    [num1, num2] = make_ints(num1, num2)

    return [num1, num2]


def post_nums():
    [num1, num2] = request_form_get()
    [num1, num2] = make_ints(num1, num2)

    return [num1, num2]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add/', methods=["GET", "POST"])
@app.route('/add', methods=["GET", "POST"])
def add_two_numbers():

    # If parameters submitted via API
    if 'param1' in request.args and 'param2' in request.args:
        [num1, num2] = api_params()

        return "Sum of {} and {} is {}".format(num1, num2, num1 + num2)

    # If user submits parameters through browser
    elif request.method == "POST":
        if not (request.form.get("param1") and request.form.get("param2")):
            return apology("Please enter two numbers to add", 400)

        [num1, num2] = post_nums()

        return render_template("added.html", param1=num1, param2=num2, sum=num1 + num2)

    # Default, with no parameters entered
    else:
        return render_template('add.html')


@app.route('/subtract/', methods=["GET", "POST"])
@app.route('/subtract', methods=["GET", "POST"])
def subtract_two_numbers():

    # If parameters submitted via API
    if 'param1' in request.args and 'param2' in request.args:
        [num1, num2] = api_params()

        return "{} minus {} is {}".format(num1, num2, num1 - num2)

    # If user submits parameters through browser
    elif request.method == "POST":
        if not (request.form.get("param1") and request.form.get("param2")):
            return apology("Please enter two numbers to subtract", 400)

        [num1, num2] = post_nums()

        return render_template("subtracted.html", param1=num1, param2=num2, sum=num1 - num2)

    # Default, with no parameters entered
    else:
        return render_template('subtract.html')


@app.route('/multiply/', methods=["GET", "POST"])
@app.route('/multiply', methods=["GET", "POST"])
def multiply_two_numbers():

    # If parameters submitted via API
    if 'param1' in request.args and 'param2' in request.args:
        [num1, num2] = api_params()

        return "{} times {} is {}".format(num1, num2, num1 * num2)

    # If user submits parameters through browser
    elif request.method == "POST":
        if not (request.form.get("param1") and request.form.get("param2")):
            return apology("Please enter two numbers to multiply", 400)

        [num1, num2] = post_nums()

        return render_template("multiplied.html", param1=num1, param2=num2, sum=num1 * num2)

    # Default, with no parameters entered
    else:
        return render_template('multiply.html')


@app.route('/divide/', methods=["GET", "POST"])
@app.route('/divide', methods=["GET", "POST"])
def divide_two_numbers():

    # If parameters submitted via API
    if 'param1' in request.args and 'param2' in request.args:
        [num1, num2] = api_params()

        return "{} divided by {} is {}".format(num1, num2, num1 / num2)

    # If user submits parameters through browser
    elif request.method == "POST":
        if not (request.form.get("param1") and request.form.get("param2")):
            return apology("Please enter two numbers to divide", 400)

        [num1, num2] = post_nums()

        return render_template("divided.html", param1=num1, param2=num2, sum=num1 / num2)

    # Default, with no parameters entered
    else:
        return render_template('divide.html')