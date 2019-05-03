from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # resJson = {}
    # resJson["hello"] = "World"
    #return resJson
    return "Hello World."

if __name__ == '__main__':
    app.run()
