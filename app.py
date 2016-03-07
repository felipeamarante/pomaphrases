from flask import Flask
import os, random
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/pomers')
def pomers():
    with open("phraselist.txt", "rw+") as fo:
        phrase = fo.readlines()[random.randint(0,55)]
        return '%s' % phrase



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)