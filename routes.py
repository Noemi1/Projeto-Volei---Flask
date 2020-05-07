from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'home.html' ,
        title="Página Inicial"
    )

@app.route('/partidas/')
def partidas():
    return render_template('partidas.html' ,
        title="Partidas"
    )

@app.route('/entrar/')
def entrar():
    return render_template('entrar.html' ,
        title="Entrar"
    )

@app.route('/detalhes/')
def detalhes():
    return render_template('partidas-detalhes.html' ,
        title="Detalhes"
    )

