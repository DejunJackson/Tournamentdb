from flask import Blueprint, jsonify, abort, request
from ..models import db, Game


bp = Blueprint('games', __name__, url_prefix='/games')

#Add games api endpoint

@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    games = Game.query.all()  # ORM performs SELECT query
    result = []
    for g in games:
        result.append(g.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response

@bp.route('', methods=['POST'])
def create():

    g = Game(
        winner=request.json['winner'],
        loser=request.json['loser'],
        winner_score=request.json['winner_score'],
        loser_score=request.json['loser_score'],
        round_id=request.json['round_id']
    )

     
    db.session.add(g)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(g.serialize())

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    g = Game.query.get_or_404(id)
    return jsonify(g.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    g = Game.query.get_or_404(id)
    try:
        db.session.delete(g)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

@bp.route('/<int:id>', methods=['PUT'])
def update(id: int):
    g = Game.query.get_or_404(id)
    g.winner=request.json['winner']
    g.loser=request.json['loser']
    g.winner_score=request.json['winner_score'],
    g.loser_score=request.json['loser_score']
    db.session.commit()
    return jsonify(g.serialize())