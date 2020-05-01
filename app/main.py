from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

names = []


class InputForm(FlaskForm):
    name = StringField("Input Your name")
    submit = SubmitField("Submit Name")


@app.route("/", methods=["GET", "POST"])
def index():
    form = InputForm()
    if request.method == "POST":
        names.append(request.form.get("name"))
    return render_template("index.html", form=form, names=names)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
