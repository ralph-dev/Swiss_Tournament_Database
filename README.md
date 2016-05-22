# Swiss_Tournament_Database
<br />
<strong> Important Files: </strong>
<br />
1) tournament.py - (Python Code which includes Queries and Joins)
<br />
2) tournament.sql - (POSTGRESQL, Contains Table initilization, Views Initilization)
<br />
3) tournament_test.py - (Python External Unit Test Cases for tournament.py)
<br />
<br />
<strong> How To Run: </strong>
<br />
Open Vagrant once installed (https://www.vagrantup.com/downloads.html)
<br />
<i> Run Command </i> ($ cd "Location where files are downloaded {Location of tournament.sql file}")
<br />
<i> Run Command </i> ($ psql)
<br />
<i> Run Command </i> ($ python tournament_test.py)
<br />
<br />
If your output looks like this, you have passed all the tests.
<br />
1. Old matches can be deleted. <br />
2. Player records can be deleted. <br />
3. After deleting, countPlayers() returns zero. <br />
4. After registering a player, countPlayers() returns 1. <br />
5. Players can be registered and deleted. <br />
6. Newly registered players appear in the standings with no matches. <br />
7. After a match, players have updated standings. <br />
8. After one match, players with one win are paired. <br />
Success!  All tests pass! <br />
