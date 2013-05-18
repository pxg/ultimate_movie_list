from flask import Flask, render_template
app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'
@app.route('/')
def home():
    name = 'PXG'
    return render_template('index.html', name=name)
    # Explain what this site is
    # Link to the main list
    # Link to the IMDB top 250 JSON
    # Link to the BFI top 10 2012
    # Link to the Oscar best picture winnners
    # Link to all Oscar winners

if __name__ == '__main__':
    app.debug = True
    app.run()
