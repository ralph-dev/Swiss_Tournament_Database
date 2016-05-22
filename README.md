# Swiss_Tournament_Database
<br />
Important Files:
<br />
1) tournament.py - (Python Code which includes Queries and Joins)
<br />
2) tournament.sql - (POSTGRESQL, Contains Table initilization, Views Initilization)
<br />
3) tournament_test.py - (Python External Unit Test Cases for tournament.py)
<br />
<br />
How To Run:
<br />
Open Vagrant once installed (https://www.vagrantup.com/downloads.html)
<br />
Run Command ($ cd "Location where files are downloaded {Location of tournament.sql file}")
<br />
Run Command ($ psql)
<br />
Run Command ($ python tournament_test.py)
<br />
If your output looks like this, you have passed all the tests.
<br />
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
