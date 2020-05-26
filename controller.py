from flask import Flask, render_template, request, url_for, redirect
from app import app
from dao import listar_partidas, listar_membros, listar_times, ver_resultado, obter_time, novo_time, remover_time, nova_partida, remover_partida, update_time


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
    time_id = request.args.get('time_id')
    partidas = listar_partidas(time_id)
    return render_template(
        'partidas.html',
        title="Partidas",
        partidas=partidas,
    )

@app.route('/partidas/remover/<partida_id>/')
def delete_partida(partida_id):
    remover_partida(partida_id)
    return redirect('/')

@app.route('/addpartidas/', methods=['GET', 'POST'])
def addpartidas():
    time_casa = request.args.get("time_id")
    casa = obter_time(time_casa)
    visita = listar_times()

    if request.method == 'POST':
        form = request.form

        nomeCasa = form.get('nomeCasa')
        pontosCasa = form.get('pontosCasa')
        nomeVisitante = form.get('nomeVisitante')
        pontosVisitantes = form.get('pontosVisitantes')
        data = form.get('data')
        localpartida = form.get('localpartida')
        duracao = form.get('duracao')
        setstotal = form.get('setstotal')
        setsvencidos = form.get('setsvencidos')
        setsperdidos = form.get('setsperdidos')
        arbitro = form.get('arbitro')
        fiscal = form.get('fiscal')
        vencedor = form.get('vencedor')

        nova_partida(
            nomeCasa,
            pontosCasa,
            nomeVisitante,
            pontosVisitantes,
            data,
            localpartida,
            duracao,
            setstotal,
            setsvencidos,
            setsperdidos,
            arbitro,
            fiscal,
            vencedor
        )
        return redirect('/')

    return render_template(
        'parts/add-partidas.html',
        casa=casa,
        visita=visita
    )


@app.route('/entrar/')
def entrar():
    return render_template(
        'entrar.html',
        title="Entrar"
    )


@app.route('/addTime/', methods=['GET', 'POST'])
def addTime():

    if request.method == 'POST':
        form = request.form

        Nome = form.get('Nome')
        Sigla = form.get('Sigla')
        Localidade = form.get('Localidade')
        Pontos = form.get('Pontos')
        Jogos = form.get('Jogos')
        Vitorias = form.get('Vitorias')
        Derrotas = form.get('Derrotas')

        novo_time(
            Nome,
            Sigla,
            Localidade,
            Pontos,
            Jogos,
            Vitorias,
            Derrotas
        )
        return redirect('/')

    return render_template(
        'parts/add-time.html',
        curso={}
    )


@app.route('/time/remover/<time_id>/')
def delete_time(time_id):
    remover_time(time_id)
    return redirect('/')


@app.route('/time/alterar/', methods=['GET', 'POST'])
def alterar_time():
    time_id = request.args.get("time_id")
    time = obter_time(time_id)

    if request.method == 'POST':
        form = request.form

        Nome = form.get('Nome')
        Sigla = form.get('Sigla')
        Localidade = form.get('Localidade')
        Pontos = form.get('Pontos')
        Jogos = form.get('Jogos')
        Vitorias = form.get('Vitorias')
        Derrotas = form.get('Derrotas')

        update_time(
            Nome,
            Sigla,
            Localidade,
            Pontos,
            Jogos,
            Vitorias,
            Derrotas,
            time_id
        )
        return redirect('/')

    return render_template(
        'parts/update_time.html',
        time=time
    )


@app.route('/addMembro/')
def addMembro():
    return render_template('parts/add-membro.html')


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