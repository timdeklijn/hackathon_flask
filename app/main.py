import os

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from joblib import load
from wtforms import SubmitField, FloatField

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

model = load(open(os.path.join("model.pk"), "rb"))
le = load(open(os.path.join("le.pk"), "rb"))

images = {
    "Setosa": "https://www.fleurproshop.com/media/img/pics/original/fleur/product/IRISSET01_G998_01.JPG?type=resize&w=610",
    "Versicolor": "https://daylily-phlox.eu/wp-content/uploads/2016/08/Iris-versicolor-1.jpg",
    "Virginica": "https://i.pinimg.com/originals/82/81/b9/8281b9a303d5c935cfebf2fac56d22c2.jpg"
}


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
        variety = le.inverse_transform(model.predict([[sep_l, sep_w, pet_l, pet_w]]))[0]
    return render_template("index.html", form=form, variety=variety, image_link=images[variety])


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
