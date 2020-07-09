from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def helloindex():
    return "Hello World from Python Flask!"

if __name__ == '__main__':
    app.run(debug = True)
