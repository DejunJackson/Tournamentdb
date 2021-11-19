from flask import Blueprint, jsonify, abort, request
from ..models import db, Team


bp = Blueprint('teams', __name__, url_prefix='/teams')

@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    teams = Team.query.all()  # ORM performs SELECT query
    result = []
    for t in teams:
        result.append(t.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response

@bp.route('', methods=['POST'])
def create():

   
    t = Team(
        name=request.json['name'],
        city=request.json['city'],
        state=request.json['state']
    )
    db.session.add(t)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(t.serialize())

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    t = Team.query.get_or_404(id)
    return jsonify(t.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    t = Team.query.get_or_404(id)
    try:
        db.session.delete(t)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

@bp.route('/<int:id>', methods=['PATCH'])
def update(id: int):
    t = Team.query.get_or_404(id)
    changed = False
    if 'name' in request.json and 'city' in request.json and 'state' in request.json:
        t.name = request.json['name']
        t.city = request.json['city']
        t.state = request.json['state']
        changed = True
    elif 'name' in request.json and 'city' in request.json:
        t.name = request.json['name']
        t.city = request.json['city']
        changed = True
    elif 'name' in request.json and 'state' in request.json:
        t.name = request.json['name']
        t.state = request.json['state']
        changed = True
    elif 'city' in request.json and 'state' in request.json:
        t.city = request.json['city']
        t.state = request.json['state']
        changed = True
    elif 'name' in request.json:
        t.name = request.json['name']
        changed = True
    elif 'city' in request.json:
        t.city = request.json['city']
        changed = True
    elif 'state' in request.json:
        t.state = request.json['state']
    db.session.commit()
    return jsonify(changed)