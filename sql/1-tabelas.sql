CREATE TABLE Equipes (
    Id          INTEGER PRIMARY KEY AUTOINCREMENT
    , Nome        VARCHAR(50) NOT NULL UNIQUE
    , Sigla       VARCHAR(10) NOT NULL UNIQUE
    , Localidade  VARCHAR(100) NOT NULL
    , Pontos INT
    , Jogos INT
    , Vitorias INT
    , Derrotas INT
  	
);

CREATE TABLE  Membros (
    Id          INTEGER PRIMARY KEY AUTOINCREMENT
    , Nome        VARCHAR(50) NOT NULL UNIQUE
    , Apelido     VARCHAR(50) NOT NULL
    , Posicao     VARCHAR(100) NOT NULL
    , Camisa      INT NOT NULL
    , Time_Id     INTEGER NOT NULL
    , FOREIGN KEY (Time_Id) REFERENCES Equipes (id)
);


CREATE TABLE  Partidas (
    Id                  INTEGER PRIMARY KEY AUTOINCREMENT
    , TimeCasa_Id           INT NOT NULL
    , TimeVisitantes_Id     INT NOT NULL
    , Pontos_Casa         INT NOT NULL
    , Pontos_Visitante INT NOT NULL
    , DataJogo                TEXT NOT NULL
    , Horario TEXT NOT NULL
    , LocalJogo TEXT NOT NULL
    , Duracao TEXT NOT NULL
    , Vencedor TEXT NOT NULL
    , SetsTotal INT NOT NULL
    , SetsVencidos INT NOT NULL
    , SetsPerdidos INT NOT NULL
    , ArbitroPrincipal TEXT NOT NULL
    , FiscalRede TEXT NOT NULL
    , FOREIGN KEY (TimeCasa_Id) REFERENCES Equipes (id)
    , FOREIGN KEY (TimeVisitantes_Id) REFERENCES Equipes (id)
);
