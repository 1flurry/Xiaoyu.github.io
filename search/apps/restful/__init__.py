from flask import Blueprint

api = Blueprint('restful', __name__)

from apps.restful import algorithm_mgmt
