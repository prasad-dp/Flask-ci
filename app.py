from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello DevOps! My Flask app is containerized"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
