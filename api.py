from flask_sqlalchemy import SQLAlchemy
from flask import Flask 



app= Flask(__name__)
app.config.from_pyfile('config.py')
db=SQLAlchemy(app)

from views import *
if __name__=='__main__':
    app.run(debug=True)