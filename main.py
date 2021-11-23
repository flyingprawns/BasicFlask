from flask import Flask

app = Flask(__name__)


# -------------- Decorator Functions ------------- #
def make_bold_wrapper(function):
    def wrapped(**kwargs):
        ret_val = function(**kwargs)
        return "<b>" + ret_val + "</b>"
    return wrapped


def make_emphasis_wrapper(function):
    def wrapped(**kwargs):
        ret_val = function(**kwargs)
        return "<em>" + ret_val + "</em>"
    return wrapped


def make_underline_wrapper(function):
    def wrapped(**kwargs):
        ret_val = function(**kwargs)
        return "<u>" + ret_val + "</u>"
    return wrapped


# -------------- Flask code ----------------------- #
@app.route("/")  # app.route is the URL. Going to that URL triggers the function.
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph!.</p>' \
           '<img src="https://media.istockphoto.com/photos/rendering-sabertooth-tiger-on-white-picture-id936062698" width=300>'


@app.route("/username/<name>/<int:number>")
@make_emphasis_wrapper
@make_bold_wrapper
@make_underline_wrapper
def greet(name, number):
    return f"Hello {name}!!! You are {number} years old?"


if __name__ == "__main__":
    app.run(debug=True)
