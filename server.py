# server for personal website

# to render flask server 
from flask import (Flask, render_template, request, flash, session, jsonify,
                   redirect)


app = Flask(__name__)
app.secret_key = "secret-key"


@app.route('/')
def show_homepage():
    return render_template('homepage.html')


if __name__ == "__main__":
    # connect_to_db(app)
    app.run(use_reloader=True, use_debugger=True)