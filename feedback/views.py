from flask import Blueprint, flash, redirect, render_template, request, url_for, send_file
from .model import FeedBackData
from .utils import getQuestions, createCSV
from .db import insertdata

home = Blueprint("homepage", __name__, url_prefix="/", static_folder="/static")
data = FeedBackData()


@home.route("/")
@home.route("/index")
def homepage():
    return render_template("home.html")


@home.route("/about")
def aboutpage():
    return render_template("about.html")


@home.route("/feedback", methods=["GET", "POST"])
def feedbackpage():
    if request.method == "POST":
        data.name = request.form.get("nametxt")
        data.email = request.form.get("emtxt")
        data.age = request.form.get("ageinput")
        data.rating = request.form.get("rating")
        data.suggestion = request.form.get("suggestbox")
        if data.rating == "default":
            flash("Please Select the Rating", "error")
            return redirect(url_for("homepage.feedbackpage"))
        else:
            return redirect(url_for("homepage.quespage"))
    else:
        return render_template("/feedbackpage/feedbackfirst.html")


@home.route("/feedback/ques", methods=["POST", "GET"])
def quespage():
    if request.method == "POST":
        data.question1 = request.form.get("question1")
        data.question2 = request.form.get("question2")
        data.question3 = request.form.get("question3")
        data.question4 = request.form.get("question4")
        data.question5 = request.form.get("question5")
        if insertdata(data):
            data.clear()
            return redirect(url_for("homepage.thankpage"))
        else:
            flash("Some Error Occured At Our End", "error")
            return redirect(url_for("homepage.homepage"))
    else:
        ques = getQuestions()
        return render_template("/feedbackpage/feedbackques.html", ques=ques)


@home.route("/thankyou")
def thankpage():
    return render_template("/thankyou.html")


@home.route("/generate")
async def generatecsv():
    collected = await createCSV()
    if collected[0]:
        return send_file(collected[1], download_name="data.csv")
    else:
        flash("Cannot Generate CSV File at this Time", "error")
        return redirect(url_for("homepage.homepage"))
