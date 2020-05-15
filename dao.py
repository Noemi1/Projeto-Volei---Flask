from flask import g
from db import query_db


def listar_times():
    return g.query_db(
        'SELECT * FROM Equipes ORDER BY Pontos DESC'
    )


def obter_time(time_id):
    return g.query_db(
        'SELECT * FROM Equipes WHERE Id = ?',
        [time_id],
        one=True
    )


def listar_membros(time_id):
    return g.query_db(
        'SELECT * FROM Membros WHERE Time_Id = ?',
        [time_id],
    )


def listar_partidas(time_id):
    return g.query_db(
        '''
            SELECT *
              FROM Partidas
               INNER JOIN Equipes on Equipes.Id == Partidas.TimeVisitantes_Id
             WHERE TimeCasa_Id = ?
        ''',
        [time_id]
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