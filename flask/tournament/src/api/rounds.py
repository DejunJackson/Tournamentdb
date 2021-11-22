from flask import Blueprint, jsonify, abort, request
from ..models import db, Round


bp = Blueprint('rounds', __name__, url_prefix='/rounds')

#add rounds api endpoint

@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    rounds = Round.query.all()  # ORM performs SELECT query
    result = []
    for r in rounds:
        result.append(r.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response

@bp.route('', methods=['POST'])
def create():

    r = Round(
        round_number=request.json['round_number'],
        winner=request.json['winner'],
        loser=request.json['loser'],
    )

     
    db.session.add(r)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(r.serialize())

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    r = Round.query.get_or_404(id)
    return jsonify(r.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    r= Round.query.get_or_404(id)
    try:
        db.session.delete(r)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

@bp.route('/<int:id>', methods=['PUT'])
def update(id: int):
    r = Round.query.get_or_404(id)
    r.round_number=request.json['round_number']
    r.winner=request.json['winner']
    r.loser=request.json['loser']
    db.session.commit()
    return jsonify(r.serialize())