from flask import Flask
import random
app = Flask(__name__)

with open("phraselist.txt", "r") as fo:
    num_lines = sum(1 for _ in fo)
print "Quantidade de linhas: " + str(num_lines)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/pomers')
def pomers():
    with open("phraselist.txt", "r") as fo:
        phrase = fo.readlines()[random.randint(0,num_lines-1)]
        return '%s' % phrase

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

