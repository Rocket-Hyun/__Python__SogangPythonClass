from flask import Flask, request
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    with open("log.txt", "a") as f:
        dstr = datetime.datetime.now()
        f.write("%s, " % (dstr))
        for p in request.args:
            f.write("%s, %s,  " % (p, request.args[p]))
        f.write("\n");
    return 'I got: a='

@app.route('/cakes')
def cakes():
    return '<html><head></head><body><h1>Yummy cakes!</h1></body></html>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 
