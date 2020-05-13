from flask import Flask, render_template, request
from equipes import equipes 
from partidas import jogos
from membros import membros
import json

app = Flask(__name__)

equip = []
for i in equipes:
    equipSTR = json.dumps(i)    
    equipJSON = json.loads(equipSTR)
    equip.append(equipJSON)


partid = []
for i in jogos:
    partidSTR = json.dumps(i)    
    partidJSON = json.loads(partidSTR)
    partid.append(partidJSON)


memb = []
for i in membros:
    membSTR = json.dumps(i)    
    membJSON = json.loads(membSTR)
    memb.append(membJSON)

@app.route('/')
def index():
    return render_template(
        'home.html',
        title="Página Inicial",
        equipes=equip
        
    )

@app.route('/partidas/')
def partidas():
    return render_template('partidas.html',
        title="Partidas",
        partidas=partid
    )

@app.route('/entrar/')
def entrar():
    return render_template('entrar.html',
        title="Entrar"
    )

@app.route('/detalhes/')
def detalhes():
    return render_template('partidas-detalhes.html',
        title="Detalhes",
        membrosEquipe=memb
    )


# @app.route('/partidas/<time>')
# def detalhes():
#     return render_template('partidas-detalhes.html',
#         title="Detalhes",
#         membrosEquipe=memb,
#         partidas=partid