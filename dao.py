from flask import g
from db import query_db, execute_db



def listar_membros(time_id):
    return g.query_db(
        'SELECT * FROM Membros WHERE Time_Id = ?',
        (time_id)
    )


def listar_partidas(time_id):
    return g.query_db(
        '''
            SELECT *
              FROM Partidas
               INNER JOIN Equipes on Equipes.Id = Partidas.TimeCasa_Id
             WHERE TimeCasa_Id = ?
        ''',
        [time_id],
        one=True

    )


# SELECT Equipes.Nome as Visitante
#   FROM Partidas
#    INNER JOIN Equipes on Equipes.Id == Partidas.TimeVisitantes_Id
#  WHERE TimeCasa_Id = ?
def ver_resultado(partida_id):
    return g.query_db(
        '''
            SELECT *
              FROM Partidas
             WHERE Id = ?
        ''',
        [partida_id],
        one=True
    )
#  SELECT *, Equipes.Nome
#               FROM Partidas
#                 INNER JOIN Equipes on Equipes.Id == Partidas.TimeVisitantes_Id
#              WHERE Id = ?
#         ''',


def listar_times():
    return g.query_db(
        'SELECT * FROM Equipes ORDER BY Pontos DESC'
    )


def obter_time(time_id):
    return g.query_db(
        '''SELECT * FROM Equipes WHERE Id = ?''',
        [time_id],
        one=True
    )


def novo_time(nome, sigla, localidade, pontos, jogos, vitorias, derrotas):
    execute_db(
        ''' INSERT INTO Equipes (Nome, Sigla, Localidade, Pontos, Jogos, Vitorias, Derrotas)
            VALUES (?, ?, ?, ?, ?, ? , ?) ''',
        (nome, sigla, localidade, pontos, jogos, vitorias, derrotas)
    )


def remover_time(time_id):
    execute_db(
        ''' DELETE FROM Equipes WHERE Id = ? ''',
        (time_id)
    )


def update_time(nome, sigla, localidade, pontos, jogos, vitorias, derrotas, time_id):
    execute_db(
            '''
            UPDATE Equipes
            SET Nome = ?,
                 Sigla = ?,
                 Localidade = ?,
                 Pontos = ?,
                 Jogos = ?,
                 Vitorias = ?,
                 Derrotas = ?
            WHERE Id = ?
              ''',
        (nome, sigla, localidade, pontos, jogos, vitorias, derrotas, time_id)
    )


def nova_partida(idTimeCasa, pontosCasa, idTimeVisita, pontosVisitantes, data, localpartida, duracao, setstotal, setsvencidos, setsperdidos, arbitro, fiscal, vencedor):
    execute_db(
        '''
        INSERT INTO Partidas
        (TimeCasa_Id, TimeVisitantes_Id, Pontos_Casa, Pontos_Visitante, DataJogo, LocalJogo, Duracao, SetsTotal, SetsVencidos, SetsPerdidos, ArbitroPrincipal, FiscalRede, Vencedor)
        VALUES
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (idTimeCasa, idTimeVisita, pontosCasa, pontosVisitantes, data, localpartida, duracao, setstotal, setsvencidos, setsperdidos, arbitro, fiscal, vencedor)
    )


def remover_partida(partida_id):
    execute_db(
        ''' DELETE FROM Partidas WHERE Id = ? ''',
        (partida_id)
    )
