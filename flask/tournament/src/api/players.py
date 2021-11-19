from flask import Blueprint, jsonify, abort, request
from ..models import db, Player


bp = Blueprint('players', __name__, url_prefix='/players')
