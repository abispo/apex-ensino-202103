
from flask import Flask

# Precisamos criar o objeto Flask que vai representar a nossa
# aplicação
app = Flask(__name__)


# Dessa maneira criamos as rotas na nossa aplicação, ou endpoints.
# Podemos atribuir mais de uma rota(endpoint) a uma função(view)
@app.route('/')
@app.route('/index')
def index():
    return "Olá! Estou aprendendo Flask."


# Quando queremos passar um argumento na rota, utilizamos a sintaxe
# <argumento>. Esse argumento deve ser passado também para a função.
@app.route('/hello/<username>')
def hello_username(username):
    return f"Hello {username}"


# Podemos fazer o 'cast' (conversão) do argumento passado para o
# tipo que desejarmos.
@app.route('/double/<int:num>')
def double_num(num):
    return f"{num * num}s"


if __name__ == '__main__':
    app.run()
