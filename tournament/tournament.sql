-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Resets the .sql file
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

-- Creates a table called Players with two columns (id, name)
CREATE TABLE Players (
    id SERIAL primary key,
    name varchar(255)
);

-- Creates a table called Matches with four columns (id, winner, loser, draw)
CREATE TABLE Matches (
    id SERIAL PRIMARY KEY,
    winner int REFERENCES Players(id),
    loser int REFERENCES Players(id)
);


-- Wins View shows number of wins for each Player
CREATE VIEW Wins AS
    SELECT players.id, COUNT(matches.id) AS n
    FROM players
    LEFT JOIN (SELECT * FROM matches) as matches
    ON players.id = matches.winner
    GROUP BY players.id;

-- Count View shows number of matches for each Player
CREATE VIEW Count AS
    SELECT players.id, Count(matches.id) AS n
    FROM players
    LEFT JOIN matches
    ON players.id = matches.winner OR players.id = matches.loser
    GROUP BY players.id;

-- Standings View shows number of wins and matches for each Player
CREATE VIEW Standings AS
    SELECT players.id,players.name,wins.n as wins,count.n as matches
    FROM players, count, wins
    WHERE players.id = wins.id and wins.id = count.id;