from flask import Flask, render_template, request, redirect, url_for, flash
from elasticsearch import Elasticsearch
from validator import is_valid_cnpj, is_valid_cep, is_valid_telephone, is_valid_email
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

es = Elasticsearch([os.getenv('ELASTICSEARCH_HOST')])

index_name = 'estabelecimentos9'
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

    mapping = {
        'properties': {
            'CNPJ': {'type': 'keyword'},
            'Nome': {'type': 'text'},
            'CEP': {'type': 'keyword'},
            'Telefone': {'type': 'keyword'},
            'Email': {'type': 'keyword'},
        }
    }
    es.indices.put_mapping(index=index_name, body=mapping)


@app.route('/')
def index():
    result = es.search(index=index_name, body={'query': {'match_all': {}}})
    estabelecimentos = [hit['_source'] for hit in result['hits']['hits']]
    return render_template('index.html', estabelecimentos=estabelecimentos)

@app.route('/add', methods=['GET', 'POST'])
def add():
     
    if request.method == 'POST':
        cnpj = request.form['cnpj']
        nome = request.form['nome']
        cep = request.form['cep']
        telefone = request.form['telefone']
        email = request.form['email']
        if not is_valid_cnpj(cnpj):
            flash('CNPJ inválido.')
            return redirect(url_for('add'))
        if not is_valid_cep(cep):
            flash('CEP inválido.')
            return redirect(url_for('add'))
        if not is_valid_telephone(telefone):
            flash('Telefone inválido.')
            return redirect(url_for('add'))
        if not is_valid_email(email):
            flash('Email inválido.')
            return redirect(url_for('add'))
        doc = {
            'CNPJ': cnpj,
            'Nome': nome,
            'CEP': cep,
            'Telefone': telefone,
            'Email': email
        }
        es.index(index=index_name, body=doc)
        flash('Estabelecimento adicionado com sucesso.')
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    result = es.get(index=index_name, id=id)
    if not result['found']:
        return redirect(url_for('page_not_found'))
    estabelecimento = result['_source']
    if request.method == 'POST':  
        cnpj = request.form['cnpj']
        nome = request.form['nome']
        cep = request.form['cep']
        telefone = request.form['telefone']
        email = request.form['email']
        if not is_valid_cnpj(cnpj):
            flash('CNPJ inválido.')
            return redirect(url_for('edit', id=id))
        if not is_valid_cep(cep):
            flash('CEP inválido.')
            return redirect(url_for('edit', id=id))
        if not is_valid_telephone(telefone):
            flash('Telefone inválido.')
            return redirect(url_for('edit', id=id))
        if not is_valid_email(email):
            flash('Email inválido.')
            return redirect(url_for('edit', id=id))

        updated_doc = {
            'CNPJ': cnpj,
            'Nome': nome,
            'CEP': cep,
            'Telefone': telefone,
            'Email': email
        }
        es.update(index=index_name, id=id, body=updated_doc)
        flash('Estabelecimento atualizado com sucesso.')
        return redirect(url_for('index'))

    return render_template('edit.html', estabelecimento=estabelecimento)

      
@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    es.delete(index=index_name, id=id)
    flash('Estabelecimento removido com sucesso.')
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
