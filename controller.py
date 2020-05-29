from flask import Flask, render_template, request, url_for, redirect
from app import app
from dao import *

@app.route('/')
def index():
    return redirect(url_for('listar_times'))
    
# Times ------------------------------------------------------------------------------------------------------------------------------  #
@app.route('/admin/times')
def listar_times():
    equipes = get_times()
    return render_template(
        'home.html',
        title="Página Inicial",
        equipes=equipes,
    )

@app.route('/admin/time/novo', methods=['GET', 'POST'])
def adicionar_time():
    if request.method == 'POST':
        form = request.form
        Nome = form.get('Nome')
        Sigla = form.get('Sigla')
        Localidade = form.get('Localidade')
        Pontos = form.get('Pontos')
        Jogos = form.get('Jogos')
        Vitorias = form.get('Vitorias')
        Derrotas = form.get('Derrotas')

        add_time(
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
        title='Adicionar'
    )

@app.route('/admin/alterar/<id_time>', methods=['GET', 'POST'])
def alterar_time(id_time):
    time = get_time(id_time)

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
            id_time
        )
        return redirect('/')

    return render_template(
        'parts/update-time.html',
        title='Alterar time',
        time=time
    )

@app.route('/admin/times/remover/<id_time>/')
def remover_time(id_time):
    delete_time(id_time)
    return redirect('/')

# Fim Times ------------------------------------------------------------------------------------------------------------------------------  #

# Partidas ------------------------------------------------------------------------------------------------------------------------------  #

@app.route('/admin/partidas')
def listar_partidas():
    time_id = request.args.get('id_time')
    partidas = get_partidas(time_id)
    timeCasa = get_time(time_id)
    return render_template(
        'partidas.html',
        title="Partidas",
        partidas=partidas,
        timeCasa=timeCasa
    )

@app.route('/admin/partidas/novo', methods=['GET', 'POST'])
def adicionar_partida():
    id_time = request.args.get("id_time")
    casa = get_time(id_time)
    visita = times_menosUm(id_time)
    partidas = get_partidas(id_time)

    if request.method == 'POST':
        form = request.form
        TimeCasa_Id = form.get('TimeCasa_Id')
        TimeVisitantes_Id = form.get('TimeVisitantes_Id')
        Pontos_Casa = form.get('Pontos_Casa')
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

        add_partida(
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
            Vencedor
        )
        return redirect( url_for( 'listar_partidas', id_time=TimeCasa_Id))

    return render_template(
        'parts/add-partidas.html',
        title='Adicionar',
        casa=casa,
        visita=visita,
        partidas=partidas,
        timeCasa=casa
    )

@app.route('/admin/partidas/remover/<partida_rowId>/')
def remover_partida(partida_rowId):
    partida = get_partida(partida_rowId)
    timeCasaId = partida['TimeCasa_Id']
    delete_partida(partida_rowId)
    partidas = get_partidas(timeCasaId)
    return redirect( url_for( 'listar_partidas', id_time=timeCasaId, partidas=partidas ))

@app.route('/admin/partidas/alterar/<partida_rowId>', methods=['GET', 'POST'])
def alterar_partida(partida_rowId):
    partida = obter_partida(partida_rowId)
    times = get_times()
    time_id = partida['TimeCasa_Id']
    casa = get_time(time_id)

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
        Partida_rowId = form.get('Partida_rowId')

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
            Partida_rowId
        )
        return redirect(url_for('listar_partidas/?id_time=' + TimeCasa_Id))

    return render_template(
        'parts/update-partida.html',
        title='Alterar',
        partida=partida,
        times=times,
        casa=casa,

    )


@app.route('/admin/detalhes/<partida_rowId>') 
def detalhes(partida_rowId):
    detalhesPartida = ver_resultado(partida_rowId)
    equipeCasa = listar_membros(detalhesPartida['TimeCasa_Id'])
    equipeAdversaria = listar_membros(detalhesPartida['TimeVisitantes_Id'])
    timeCasa = get_time(detalhesPartida['TimeCasa_Id'])
    timeAdversario = get_time(detalhesPartida['TimeVisitantes_Id'])
    return render_template('partidas-detalhes.html',
                           title="Detalhes",
                           equipeCasa=equipeCasa,
                           equipeAdversaria=equipeAdversaria,
                           detalhesPartida=detalhesPartida,
                           timeCasa=timeCasa,
                           timeAdversario=timeAdversario

                           )

# Fim Partidas ------------------------------------------------------------------------------------------------------------------------------  #

# Entrar ------------------------------------------------------------------------------------------------------------------------------  #
@app.route('/entrar/')
def entrar():
    return render_template(
        'entrar.html',
        title="Entrar"
    )

# Fim Entrar ------------------------------------------------------------------------------------------------------------------------------  #

# Membros ------------------------------------------------------------------------------------------------------------------------------  #
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
    time = get_time(time_id)
    membros = obter_membros(time_id)
    return render_template(
        'membros.html',
        time=time,
        time_id=time_id,
        membros=membros,
        title="Membros"
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
    
# Fim Membros ------------------------------------------------------------------------------------------------------------------------------  #