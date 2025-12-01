from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
import json


app  = Flask(__name__)

with open('usuarios.json', 'r', encoding='utf-8') as f:
    usuarios = json.load(f)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']

        for usuario in usuarios:
            if usuario['nome'] == nome:
                if check_password_hash(usuario['senha'], senha):
                    return 'acesso permitido'
                else:
                    return f'acesso negado | Senha: {senha}'

    return render_template('login.html')



@app.route('/cadastrar', methods=['POST', 'GET'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['username']
        email = request.form['email']
        senha = generate_password_hash(request.form['password'])

        usuario = {}
        usuario['nome'] = nome
        usuario['email'] = email
        usuario['senha'] = senha

        usuarios.append(usuario)

        with open('usuarios.json', 'w', encoding='utf-8') as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)


        # return f'usuario: {nome} | gmail: {email} | senha: {senha}'
        return render_template('login.html')

    return render_template('cadastrar.html')


#fazer atividade

if __name__  == '__main__':
    app.run(debug=True)