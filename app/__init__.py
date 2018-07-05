import os
from flask import Flask, render_template, send_from_directory
from sucuri import rendering

app = Flask(__name__)

@app.route("/")
def index():
    param = { 'body': rendering.template('app/main.suc') }
    return render_template('index.html', **param)

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run()
