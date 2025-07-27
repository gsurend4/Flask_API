from flask import Flask
import numpy

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World! Hi"

@app.route('/<name>')
def test(name):
    return "Hi {}".format(name)

if __name__ == '__main__':
    app.run(port=8000, debug=True)

# Use either 1 or 2 to resolve this issue.
# 1. Changed the port to solve the access denied issue.
# 2. chrome://net-internals/#sockets. --> To flush the sockets if access denied issue pops up.