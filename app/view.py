from flask import render_template, request
from transformers import pipeline
from app import app

# Load the Hugging Face pipeline
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        result = classifier(text)[0]
        return render_template("index.html", classification=result["label"])
    return render_template("index.html", classification=None)
