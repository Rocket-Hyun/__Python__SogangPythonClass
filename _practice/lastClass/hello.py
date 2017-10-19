from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><head><title>제목</title></head><body><h1>GO!</h1></body></html>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
