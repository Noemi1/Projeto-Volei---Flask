from flask import g
from db import query_db, execute_db

# Times ------------------------------------------------------------------------------------------------------------------------------  #
# Listar Times
def get_times():
    return g.query_db(
        'SELECT * FROM Equipes ORDER BY Pontos DESC'
    )

# Get time
def get_time(time_id):
    return g.query_db(
        '''SELECT * FROM Equipes WHERE Id = ?''',
        [time_id],
        one=True
    )

# Add Time
def add_time(nome, sigla, localidade, pontos, jogos, vitorias, derrotas):
    execute_db(
        ''' INSERT INTO Equipes (Nome, Sigla, Localidade, Pontos, Jogos, Vitorias, Derrotas)
            VALUES (?, ?, ?, ?, ?, ? , ?) ''',
        (nome, sigla, localidade, pontos, jogos, vitorias, derrotas)
    )

# Delete Time
def delete_time(time_id):
    execute_db(
        ''' DELETE FROM Equipes WHERE Id = ? ''',
        (time_id)
    )

# Update Time
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

# Fim Times ------------------------------------------------------------------------------------------------------------------------------  #

def listar_membros(time_id):
    return g.query_db(
        'SELECT * FROM Membros WHERE Time_Id = ?',
        [time_id]
    )


# ----------------------------------------PARTIDAS ---------------------------

def nova_partida(TimeCasa_Id, Pontos_Casa, TimeVisitantes_Id, Pontos_Visitante, DataJogo, LocalJogo, Duracao, SetsTotal, SetsVencidos, SetsPerdidos, ArbitroPrincipal, FiscalRede, Vencedor):
    execute_db(
        '''
        INSERT INTO Partidas
        (TimeCasa_Id, TimeVisitantes_Id, Pontos_Casa, Pontos_Visitante, DataJogo, LocalJogo, Duracao, SetsTotal, SetsVencidos, SetsPerdidos, ArbitroPrincipal, FiscalRede, Vencedor)
        VALUES
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (TimeCasa_Id, TimeVisitantes_Id, Pontos_Casa, Pontos_Visitante, DataJogo, LocalJogo,
         Duracao, SetsTotal, SetsVencidos, SetsPerdidos, ArbitroPrincipal, FiscalRede, Vencedor)
    )


def remover_partida(partida_id):
    execute_db(
        ''' DELETE FROM Partidas WHERE Id = ? ''',
        (partida_id)
    )
    oi = g.query_db(
        ''' SELECT *  FROM Partidas '''
    )


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


def listar_partidas(time_id):
    partidas = g.query_db(
        '''
            SELECT *
              FROM Partidas
               INNER JOIN Equipes on Equipes.Id = Partidas.TimeCasa_Id
             WHERE TimeCasa_Id = ?
        ''',
        [time_id]
    )
    return partidas


def update_partida(TimeCasa_Id, TimeVisitantes_Id, Pontos_Casa, Pontos_Visitante, DataJogo, LocalJogo, Duracao, SetsTotal, SetsVencidos, SetsPerdidos, ArbitroPrincipal, FiscalRede, Vencedor, Partida_Id):
    return execute_db(
        '''
            UPDATE Partidas
            SET 
                TimeCasa_Id = ?,  
                TimeVisitantes_Id = ?,  
                Pontos_Casa = ?,  
                Pontos_Visitante = ?,  
                DataJogo = ?,  
                LocalJogo = ?,  
                Duracao = ?,  
                SetsTotal = ?,  
                SetsVencidos = ?,  
                SetsPerdidos = ?,  
                ArbitroPrincipal = ?,  
                FiscalRede = ?,  
                Vencedor = ?
            WHERE Id = ?
              ''',
        (TimeCasa_Id, TimeVisitantes_Id, Pontos_Casa, Pontos_Visitante, DataJogo, LocalJogo, Duracao,
         SetsTotal, SetsVencidos, SetsPerdidos, ArbitroPrincipal, FiscalRede, Vencedor, Partida_Id)
    )


def obter_partida(id_partida):
    return g.query_db(
        ''' SELECT *  FROM Partidas
            WHERE Id = ?
        ''',
        [id_partida],
        one=True
    )


def novo_membro(Nome, Apelido, Posicao, Camisa, Time_Id):
    execute_db(
        '''
        INSERT INTO Membros (Nome, Apelido, Posicao, Camisa, Time_Id)
        VALUES
        (?, ?, ?, ?, ?) ''',
        (Nome, Apelido, Posicao, Camisa, Time_Id)
    )

def obter_membros(time_id):
    return g.query_db(
        '''
        SELECT * FROM Membros
                    WHERE Time_Id = ?
        ''',
        [time_id]
    )

def remover_membro(membro):
    execute_db(
        '''
        DELETE FROM Membros WHERE Id = ?
        ''',
        (membro)
    )

def membro_obter(membro):
    return g.query_db(
        ''' SELECT * FROM Membros WHERE Id = ? ''',
        [membro],
        one=True
    )

def alterar_membro(Nome, Apalido, Posicao, Camisa, Id_Membro):
    execute_db(
        '''
        UPDATE Membros
        SET Nome = ? ,
            Apelido = ? ,
            Posicao = ? ,
            Camisa = ? 
        WHERE Id = ?
        ''',
        (Nome, Apalido, Posicao, Camisa, Id_Membro)
    )


def times_menosUm(time_id):
    times = g.query_db(
        '''
            SELECT *
              FROM Equipes
             WHERE Id != ?
        ''',
        [time_id]
    )
    return times

