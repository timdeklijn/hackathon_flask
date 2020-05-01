import os

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from joblib import load
from wtforms import SubmitField, FloatField

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

model = load(open(os.path.join("model.pk"), "rb"))
le = load(open(os.path.join("le.pk"), "rb"))


class IrisForm(FlaskForm):
    sepal_length = FloatField("Sepal Length")
    sepal_width = FloatField("Sepal Width")
    petal_length = FloatField("Petal Length")
    petal_width = FloatField("Petal Width")
    submit = SubmitField("Submit Measured Flower")


@app.route("/", methods=["GET", "POST"])
def index():
    variety = None
    form = IrisForm()
    if request.method == "POST":
        sep_l = request.form.get("sepal_length")
        sep_w = request.form.get("sepal_width")
        pet_l = request.form.get("petal_length")
        pet_w = request.form.get("petal_width")
        variety = le.inverse_transform(model.predict([[sep_l, sep_w, pet_l, pet_w]]))
    return render_template("index.html", form=form, variety=variety)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
