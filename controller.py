from flask import Flask, render_template, request, url_for
from app import app
from dao import listar_partidas, listar_membros, listar_times, ver_resultado, obter_time

@app.route('/')
def index():
    equipes = listar_times()
    return render_template(
        'home.html',
        title="Página Inicial",
        equipes=equipes,
    )


@app.route('/partidas') # Nao consigo colocar o /partidas/<time_id>
def partidas():
    time_id = request.args.get("time_id")
    partidas = listar_partidas(time_id)
    casa = obter_time(time_id)
    return render_template('partidas.html',
        title="Partidas",
        partidas=partidas,
        casa=casa
        
    )

@app.route('/entrar/')
def entrar():
    return render_template('entrar.html',
        title="Entrar"
    )

@app.route('/detalhes/') # Nao consigo colocar o /detalhes/<id>
def detalhes():
    partidaId = request.args.get("detalhes")
    detalhesPartida = ver_resultado(partidaId)
    equipeCasa = listar_membros(detalhesPartida['TimeCasa_Id'])
    equipeAdversaria = listar_membros(detalhesPartida['TimeVisitantes_Id'])
    timeCasa = obter_time(detalhesPartida['TimeCasa_Id'])
    timeAdversario = obter_time(detalhesPartida['TimeVisitantes_Id'])
    return render_template('partidas-detalhes.html',
        title="Detalhes",
        equipeCasa=equipeCasa,
        equipeAdversaria=equipeAdversaria,
        detalhes=detalhesPartida,
        timeCasa = timeCasa,
        timeAdversario=timeAdversario

    )