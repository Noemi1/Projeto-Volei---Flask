from flask import Flask, render_template, request, url_for, redirect
from app import app
from dao import listar_partidas, listar_membros, listar_times, ver_resultado, obter_time, novo_time, remover_time, nova_partida, remover_partida, update_time, obter_partida, update_partida, novo_membro, obter_membros, remover_membro, membro_obter, alterar_membro, times_menosUm

@app.route('/')
def index():
    equipes = listar_times()
    return render_template(
        'home.html',
        title="Página Inicial",
        equipes=equipes,
    )


@app.route('/time/remover/<time_id>/')
def delete_time(time_id):
    remover_time(time_id)
    return redirect('/')


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
        curso={},
        title='Alterar'
    )


@app.route('/alterar/', methods=['GET', 'POST'])
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
        'parts/update-time.html',
        title='Alterar time',
        time=time
    )

# ----------------------- PARTIDAS ----------------------------


@app.route('/partidas')  # Nao consigo colocar o /partidas/<time_id>
def partidas():
    time_id = request.args.get('time_id')
    partidas = listar_partidas(time_id)
    timeCasa = obter_time(time_id)
    return render_template(
        'partidas.html',
        title="Partidas",
        partidas=partidas,
        timeCasa=timeCasa
    )


@app.route('/partidas/remover/<partida_id>/')
def delete_partida(partida_id):
    remover_partida(partida_id)
    return redirect('/')


@app.route('/addpartidas/', methods=['GET', 'POST'])
def addpartidas():
    time_casa = request.args.get("time_id")
    casa = obter_time(time_casa)
    visita = times_menosUm(time_casa)
    # visita = listar_times()

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
        visita=visita,
        title='Alterar'
    )


# --------------- ENTRAR-------------

@app.route('/entrar/')
def entrar():
    return render_template(
        'entrar.html',
        title="Entrar"
    )


# --------------- MEMBROS -------------
@app.route('/addMembro/', methods=['GET', 'POST'])
def add_membro():
    time_id = request.args.get('time_id')

    if request.method == 'POST':
        form = request.form

        Nome = form.get('Nome')
        Apelido = form.get('Apelido')
        Posicao = form.get('Posicao')
        Camisa = form.get('Camisa')
        Time_Id = form.get('Time_Id')

        novo_membro(
            Nome,
            Apelido,
            Posicao,
            Camisa,
            Time_Id
        )
        return redirect('/')

    return render_template(
        'parts/add-membro.html',
        time_id=time_id
    )

    
@app.route('/membros')
def membros():
    time_id = request.args.get('time_id')
    time = obter_time(time_id)
    membros = obter_membros(time_id)
    return render_template(
        'membros.html',
        time=time,
        time_id=time_id,
        membros=membros,
        title="Membros"
    )


# ------------- DETALHES ---------------


@app.route('/detalhes/')  # Nao consigo colocar o /detalhes/<id>
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
                           timeCasa=timeCasa,
                           timeAdversario=timeAdversario

                           )


# ------------- ALTERAR PARTIDAS ---------------
@app.route('/alt-partidas/', methods=['GET', 'POST'])
def alt_partidas():
    partida_id = request.args.get('partida_id')
    partida = obter_partida(partida_id)
    times = listar_times()
    casa = obter_time(partida_id)

    if request.method == 'POST':
        form = request.form
        TimeCasa_Id = form.get('TimeCasa_Id')
        Pontos_Casa = form.get('Pontos_Casa')
        TimeVisitantes_Id = form.get('TimeVisitantes_Id')
        Pontos_Visitante = form.get('Pontos_Visitante')
        DataJogo = form.get('DataJogo')
        LocalJogo = form.get('LocalJogo')
        Duracao = form.get('Duracao')
        SetsTotal = form.get('SetsTotal')
        SetsVencidos = form.get('SetsVencidos')
        SetsPerdidos = form.get('SetsPerdidos')
        ArbitroPrincipal = form.get('ArbitroPrincipal')
        FiscalRede = form.get('FiscalRede')
        Vencedor = form.get('Vencedor')
        Partida_Id = form.get('Partida_Id')

        update_partida(
            TimeCasa_Id,
            TimeVisitantes_Id,
            Pontos_Casa,
            Pontos_Visitante,
            DataJogo,
            LocalJogo,
            Duracao,
            SetsTotal,
            SetsVencidos,
            SetsPerdidos,
            ArbitroPrincipal,
            FiscalRede,
            Vencedor,
            Partida_Id
        )
        return redirect('/')

    return render_template(
        'parts/update-partida.html',
        partida=partida,
        times=times,
        casa=casa,
        title='Alterar'

    )

@app.route('/deletemembro')
def delete_membro():
    membro = request.args.get('membro')
    remover_membro(membro)
    return redirect('/')


@app.route('/updatemembro/', methods=['GET', 'POST'])
def update_membro():
    membro_id = request.args.get('membro_id')
    membro = membro_obter(membro_id)
    print(membro)

    if request.method == 'POST':
        form = request.form

        Nome = form.get('Nome')
        Apelido = form.get('Apelido')
        Posicao = form.get('Posicao')
        Camisa = form.get('Camisa')

        alterar_membro(
            Nome,
            Apelido,
            Posicao,
            Camisa,
            membro_id
        )
        return redirect('/')

    return render_template(
        'parts/update-membro.html',
        membro=membro
    )