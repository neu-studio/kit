from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecretkey'

@app.route('/endpoint1')
def end1():
    return "Hi, this is endpoint 1", 200

@app.route('/endpoint2')
def end2():
    return "Hi endpoint 2 visitor", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)