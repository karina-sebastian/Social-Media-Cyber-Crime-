from flask import Flask, render_template, request
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained summarization pipeline
summarizer = pipeline("summarization", model="t5-small")

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        # Get the victim text input from the form
        victim_text = request.form["victim_text"]
        # Generate the summary using the pipeline
        if len(victim_text) > 0:
            summary = summarizer(victim_text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
        else:
            summary = "Please enter the text of the victim."
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
