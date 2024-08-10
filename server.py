from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


# Home route
@app.route("/")
def home():
    return render_template("index.html")


# Prediction route


if __name__ == "__main__":
    app.run(debug=True)

