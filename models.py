from api import db
from flask_sqlalchemy import SQLAlchemy
from flask import Flask ,render_template,request,redirect,session,flash, url_for

class Lembrete (db.Model):
    id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    nome=db.Column(db.String(50),nullable=False)
    data=db.Column(db.Date,nullable=False)
    
    
    def __repr__(self):
        return '<Name %r>' % self.name

