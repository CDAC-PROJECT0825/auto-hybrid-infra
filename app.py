from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "🚀 Flask Application is Running!"


@app.route("/health")
def health():
    return jsonify(status="UP", message="Application is healthy")


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify(
        operation="addition",
        a=a,
        b=b,
        result=a + b
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
