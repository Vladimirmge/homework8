from flask import Flask

app = Flask(__name__)

def cal (a, b):
    c = a + b
    return c

@app.route("/")
def index():

    return "This is a paymet page %"%(cal(10,15))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
    