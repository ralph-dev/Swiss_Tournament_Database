#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connection_up():
    """Returns the cursor so SQL functions can be run"""
    conn = connect()
    c = conn.cursor()
    return (c, conn)

def connection_down(conn):
    """Closes the cursor"""
    conn.commit()
    conn.close()

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    (c, conn) = connection_up()
    c.execute("DELETE FROM Matches")
    connection_down(conn)


def deletePlayers():
    """Remove all the player records from the database."""
    (c, conn) = connection_up()
    c.execute("DELETE FROM Players")
    connection_down(conn)

def countPlayers():
    """Returns the number of players currently registered."""
    (c, conn) = connection_up()
    c.execute("SELECT count(id) FROM Players")
    num_players = c.fetchone()[0]
    conn.close()
    return num_players

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    (c, conn) = connection_up()
    c.execute("INSERT INTO players (name) VALUES (%s)",(name,))
    connection_down(conn)

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    (c, conn) = connection_up()
    c.execute("SELECT id, name, wins, matches from Standings ORDER BY wins DESC")
    list_of_players = c.fetchall()
    conn.close()
    return list_of_players


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    (c, conn) = connection_up()
    c.execute("INSERT INTO Matches (winner, loser) VALUES (%s, %s)", (winner, loser))
    connection_down(conn)

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    player_pairs = playerStandings()
    pairings = []
    for i in range(0,len(player_pairs),2):
        pairings.append((player_pairs[i][0], player_pairs[i][1], player_pairs[i+1][0], player_pairs[i+1][1]))

    return pairings

