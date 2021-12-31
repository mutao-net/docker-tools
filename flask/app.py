from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://user:pass@db_container:3306/test"

db = SQLAlchemy(app)

from model import User

@app.route('/')
def main():
    res = []
    result = User.query.all()
    for r in result:
        print (r.__dict__)
        res.append(r.__dict__)
    return str(res)

@app.route('/hello')
def hello():
    hello = "Hello world"
    return hello

if __name__ == "__main__":
    app.run()