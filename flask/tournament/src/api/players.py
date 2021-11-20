from flask import Blueprint, jsonify, abort, request
from ..models import db, Player


bp = Blueprint('players', __name__, url_prefix='/players')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    players = Player.query.all()  # ORM performs SELECT query
    result = []
    for p in players:
        result.append(p.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response

@bp.route('', methods=['POST'])
def create():

    # construct user
    p = Player(
        name=request.json['name'],
        position=request.json['position'],
        classification=request.json['classification'],
        team_id=request.json['team_id']
    )
    db.session.add(p)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(p.serialize())

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    p = Player.query.get_or_404(id)
    return jsonify(p.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    p = Player.query.get_or_404(id)
    try:
        db.session.delete(p)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

@bp.route('/<int:id>', methods=['PUT'])
def update(id: int):
    p = Player.query.get_or_404(id)
    p.name=request.json['name']
    p.position=request.json['position']
    p.classification=request.json['classification'],
    p.team_id=request.json['team_id']
    db.session.commit()
    return jsonify(p.serialize())