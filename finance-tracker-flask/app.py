from flask import Flask

app = Flask("Personal Finance Tracker")

@app.route('/')

def hello_world():
    return 'hello world'
