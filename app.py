import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        topic = request.form["topic"]
        response = openai.Completion.create(
            engine="text-davinci-001",
            prompt=generate_prompt(topic),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(topic):
    return """Tell an inappropriate joke about the given topic.

Topic: Sex
Joke: Having sex in an elevator is wrong. On so many levels.
Topic: Pregnancy
Joke: What's the difference between a pregnant woman and a lightbulb? You can unscrew a lightbulb.
Topic: {}
Joke:""".format(
        topic.capitalize()
    )
