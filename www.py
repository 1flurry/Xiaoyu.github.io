from flask import *
from apps.restful import api
import json
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.register_blueprint(api)

@app.route('/')
def index():
    return render_template("base.html")
@app.route('/about')
def resume():
    return render_template("resume.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/link')
def link():
    return render_template("link.html")

if __name__ == '__main__':

    app.run(host='127.0.0.1',debug=True)
