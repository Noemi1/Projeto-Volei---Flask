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
    equipes = get_times()
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
        return redirect(url_for('listar_times'))

    return render_template(
        'parts/add-time.html',
        title='Adicionar',
        equipes=equipes
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

@app.route('/admin/partidas/<id_time>')
def listar_partidas(id_time):
    partidas = get_partidas(id_time)
    timeCasa = get_time(id_time)
    return render_template(
        'partidas.html',
        title="Partidas",
        partidas=partidas,
        timeCasa=timeCasa
    )

@app.route('/admin/partidas/novo/<id_time>', methods=['GET', 'POST'])
def adicionar_partida(id_time):
    casa = get_time(id_time)
    visita = times_menosUm(id_time)
    partidas = get_partidas(id_time)
    times = times_menosUm(id_time)

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
        timeCasa=casa,
        times=times
    )

@app.route('/admin/partidas/remover/<id_partida>/')
def remover_partida(id_partida):
    partida = get_partida(id_partida)
    timeCasaId = partida['TimeCasa_Id']
    delete_partida(id_partida)
    partidas = get_partidas(timeCasaId)
    return redirect( url_for( 'listar_partidas', id_time=timeCasaId, partidas=partidas ))

@app.route('/admin/partidas/alterar/<id_partida>', methods=['GET', 'POST'])
def alterar_partida(id_partida):
    partida = obter_partida(id_partida)
    time_id = partida['TimeCasa_Id']
    times = times_menosUm(time_id)
    timeCasa = get_time(time_id)
    partidas = get_partidas(time_id)


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
        id_partida = form.get('id_partida')

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
            id_partida
        )
        return redirect(url_for('listar_partidas', id_time=TimeCasa_Id))

    return render_template(
        'parts/update-partida.html',
        title='Alterar',
        partida=partida,
        times=times,
        timeCasa=timeCasa,
        partidas=partidas
    )


@app.route('/admin/detalhes/<id_partida>') 
def detalhes(id_partida):
    detalhesPartida = ver_resultado(id_partida)
    equipeCasa = get_membros(detalhesPartida['TimeCasa_Id'])
    equipeAdversaria = get_membros(detalhesPartida['TimeVisitantes_Id'])
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
@app.route('/admin/membros/<id_time>')
def listar_membros(id_time):
    time = get_time(id_time)
    membros = get_membros(id_time)
    return render_template(
        'membros.html',
        time=time,
        id_time=id_time,
        membros=membros,
        title="Membros"
    )

@app.route('/admin/membros/novo/<id_time>', methods=['GET', 'POST'])
def adicionar_membro(id_time):
    membros = get_membros(id_time)
    if request.method == 'POST':
        form = request.form
        Nome = form.get('Nome')
        Apelido = form.get('Apelido')
        Posicao = form.get('Posicao')
        Camisa = form.get('Camisa')
        Time_Id = form.get('Time_Id')

        add_membro(
            Nome,
            Apelido,
            Posicao,
            Camisa,
            Time_Id
        )
        return redirect('/')

    return render_template(
        'parts/add-membro.html',
        id_time=id_time,
        membros=membros
    )
 
@app.route('/admin/membros/remover/<id_membro>')
def remover_membro(id_membro):
    membro = get_membro(id_membro)
    time = get_time(membro['Time_Id'])
    timeId = time['Id']
    delete_membro(id_membro)
    return redirect(url_for('listar_membros', id_time=timeId))


@app.route('/admin/membros/alterar/<id_membro>', methods=['GET', 'POST'])
def alterar_membro(id_membro):
    membro = get_membro(id_membro)
    timeId = membro['Time_Id']
    membros = get_membros(timeId)

    if request.method == 'POST':
        form = request.form

        Nome = form.get('Nome')
        Apelido = form.get('Apelido')
        Posicao = form.get('Posicao')
        Camisa = form.get('Camisa')

        update_membro(
            Nome,
            Apelido,
            Posicao,
            Camisa,
            id_membro
        )
        return redirect( url_for('listar_membros', id_time=timeId ))

    return render_template(
        'parts/update-membro.html',
        membro=membro,
        membros=membros,
        id_time=timeId,
        title="Alterar"
    )
    
# Fim Membros ------------------------------------------------------------------------------------------------------------------------------  #