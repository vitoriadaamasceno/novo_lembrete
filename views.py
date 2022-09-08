from flask_sqlalchemy import SQLAlchemy
from flask import Flask ,render_template,request,redirect,session,flash, url_for
from api import app,db
from models import Lembrete
from datetime import datetime,date
import time



@app.route('/')
#index
def index():
    lista=Lembrete.query.order_by(Lembrete.data) 
    return render_template('lista.html', lembrete= lista)

#criar
@app.route('/criar', methods=['POST',])
def criar():
    nome= request.form['nome'] 
    data= request.form['data']
    
    #Formatação de datas
    data_hoje= date.today().strftime('%Y-%m-%d')
    data_hoje_formatada=datetime.strptime(data_hoje, '%Y-%m-%d').date()
    data_forms= datetime.strptime(data, '%Y-%m-%d').date()

    #Validando entradas
    if nome != '':
        pass
    else:
        flash('Todos os campos devem está preenchidos!')
        return redirect(url_for('index'))
    #datas existentes
    datas= Lembrete.query.filter_by(data=data).first()
    if datas:
        novo_lembrete=Lembrete(nome=nome,data=data)
        db.session.add(novo_lembrete)
        db.session.commit() #salva a informação no banco
        flash('Lembrete com data existente,enviado com sucesso!')
        return redirect(url_for('index'))
    
    if data_forms >= data_hoje_formatada:
        novo_lembrete=Lembrete(nome=nome, data=data)
        db.session.add(novo_lembrete) 
        db.session.commit() #salva a informação
        flash('Lembrete Enviado!')
        return redirect(url_for('index'))
    else:
        flash('Só é permitido datas futuras!')
        return redirect(url_for('index'))
    


@app.route('/deletar/<int:id>')
def deletar(id):

    Lembrete.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Lembrete deletado com sucesso!')

    return redirect(url_for('index'))
