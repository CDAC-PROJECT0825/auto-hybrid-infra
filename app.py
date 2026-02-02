from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    members = [
        {"name": "Atharva Chaudhari", "prn": "250844223007"},
        {"name": "Atharva Deo", "prn": "250844223010"},
        {"name": "Rushikesh Khot", "prn": "250844223037"},
        {"name": "Saurabh Tekale", "prn": "250844223052"}
    ]
    return render_template("index.html", members=members)

if __name__ == "__main__":
    app.run(debug=True)
