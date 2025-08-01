from mercado import app
from flask import render_template, redirect, url_for, flash
from mercado.models import Item, User
from mercado.forms import CadastroForm
from mercado import db

@app.route('/')
def page_home():
    return render_template('home.html')

@app.route('/produtos')
def page_produto():
    itens = Item.query.all()
    return render_template('produtos.html', itens=itens)

@app.route('/cadastro', methods=['GET', 'POST'])
def page_cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        usuario = User(
            usuario = form.usuario.data,
            email = form.email.data,
            senha = form.senha1.data
        )

        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('page_produto'))
    
    if form.errors != {}:
        for err in form.errors.values():
            flash(f"Erro ao cadastrar usuário {err}", category="danger")



    return render_template('cadastro.html', form=form)