from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello, {request.args.get('name')}"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)