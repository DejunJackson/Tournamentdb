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
        classification=request.json['classification']
    )
    db.session.add(p)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(p.serialize())