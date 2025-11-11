from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route('/')
def index():
    return '<h1>Welcome to Flatiron Cars</h1>'

@app.route('/<string:carmodel>')
def model(carmodel):
    if carmodel in existing_models:
        return f"Flatiron {carmodel} is in our fleet!"
    if carmodel not in existing_models:
        return f"No models called {carmodel} exist in our catalog"