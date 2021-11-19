from flask import Blueprint, jsonify, abort, request
from ..models import db, Game


bp = Blueprint('games', __name__, url_prefix='/games')
