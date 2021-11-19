from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    position = db.Column(db.String(2), nullable=False)
    classification = db.Column(db.String(128), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

    def __init__(self, name: str, position: str, classification: str, team_id: int):
        self.name = name
        self.position = position
        self.classification = classification
        self.team_id = team_id
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position,
            'classification': self.classification,
            'team_id': self.team_id
        }


class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    players = db.relationship('Player', backref='team', cascade="all,delete")


    def __init__(self, name: str, city: str, state: str):
        self.name = name
        self.city = city
        self.state = state
        self.wins = 0
        self.losses = 0
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'wins': self.wins,
            'losses': self.losses
        }

class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_number = db.Column(db.Integer, nullable=False)
    winner = db.Column(db.String(128), nullable=False)
    loser = db.Column(db.String(128), nullable=False)
    winner_score = db.Column(db.Integer, nullable=False)
    loser_score = db.Column(db.Integer, nullable=False)
    round_id = db.Column(db.Integer, db.ForeignKey(
        'rounds.id'), nullable=False)


class Round(db.Model):
    __tablename__ = 'rounds'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    round_number = db.Column(db.Integer, nullable=False)
    winner = db.Column(db.String(128), nullable=False)
    loser = db.Column(db.String(128), nullable=False)
    games = db.relationship('Game', backref='round', cascade="all,delete")


teams_games = db.Table('teams_games',
                       db.Column(
                           'team_id', db.Integer,
                           db.ForeignKey('teams.id'),
                           primary_key=True
                       ),
                       db.Column(
                           'game_id', db.Integer,
                           db.ForeignKey('games.id'),
                           primary_key=True
                       )
                       )
