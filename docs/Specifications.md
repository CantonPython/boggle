# Server Documentation

## Responsibilities of server

- creates the game board
  - NOTE: this piece will be re-used on the client
- manages the state of the game
  - manages the time
  - calculates score


## Models
Lobby
  - welcome message
  - games (in progress)

Game
  - players
  - start time
  - end time
  - board
  - in progress (compute this based on start/end time)

Player
  - username
  

## Relations
Lobby `has many` games
Game `has many` players

Player `belongs to` one game


## Model Notes

### Lobby

The user's initial interaction with the server is with the lobby. 

The lobby needs to be able to make a new game, add a user to it, lock it from allowing players in after the start, and change it's state at end time

The lobby must be able to prevent access to a game's details (i.e. - board) until the start time has begun. Board isn't generated until game start time.

It is the player's responsibility to poll the server for game board availability. When client first detects game has finished they must submit words. The lobby should prevent submissions after an interval just as a validation step done on the server-side.

Need to be able to get games that have ended

### Game

Only supporting concurrent mode now. 


### Player

Unique username (enforced on server)



## Endpoints

### Lobby
Get Welcome Message

Create a game

Get List of Games not in progress

Get List of completed games (with score details)

Join a game



### Game
NOTE: all games are created by the lobby and must validate user can access it. All endpoints require username and need to validate it exists and that user is in the game


Get Game Details
- includes all game details - board, start/end time

Submit Words

Get Game Results


### Player
Register
- user gets a unique ID back. ID is used to validate in game. If user is booted/disconnects, they get new IDs and can't re-enter any game they were in that's in progress. If we need to change this we should validate by username (which could be a different person)








