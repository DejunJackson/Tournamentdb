# Tournamentdb

# Description
This is an API built using Flask, SQLAlchemy as the ORM and postgreSQL as the database. This api is designed to track players, teams, games and rounds of a college basketball tournament.

# Example API reference table

| Method    | Endpoint     | Description |  
| ----------- | ----------- | ----------|
| GET    | /players       | Returns all players |
| GET   | /players/<:id>       | Returns a specific player |
| POST  | /players        | Creates a new player with team_id, name, position, and classification |
| PUT   | /players/<:id>  | Modifies player info  |
| DEL   | /players/<:id>  | Deletes a specific player |

.
