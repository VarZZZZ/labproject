from flask import Flask,render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
#manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('hello.html')


if __name__ == '__main__':
    bootstrap.run()
