
from flask import Flask

# Precisamos criar o objeto Flask que vai representar a nossa
# aplicação
app = Flask(__name__)


# Dessa maneira criamos as rotas na nossa aplicação, ou endpoints.
@app.route('/')
def index():
    return "Olá! Estou aprendendo Flask."


if __name__ == '__main__':
    app.run()
