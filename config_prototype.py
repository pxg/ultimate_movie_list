from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
print app.config['SQLALCHEMY_DATABASE_URI']