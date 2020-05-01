import os

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
import pickle

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

names = []

model = pickle.load(open(os.path.join("model.pk"), 'rb'))


class IrisForm(FlaskForm):
    sepal_length = FloatField("Sepal Lenght")
    sepal_width = FloatField("sepal_width")
    petal_length = FloatField("petal_length")
    petal_width = FloatField("petal_width")
    submit = SubmitField("Submit Measured Flower")


@app.route("/", methods=["GET", "POST"])
def index():
    print(model)
    form = IrisForm()
    if request.method == "POST":
        names.append(request.form.get("name"))
    return render_template("index.html", form=form, names=names)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
