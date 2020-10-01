from flask_restx import Resource, Namespace
from flask import jsonify
from ..models.lab import Lab as model_lab
from ..util.dto import LabDto

lab = LabDto.api

@lab.route('/', methods=['GET'])
class Lab(Resource):
    def get(self):
        """Query all lab information"""
        all_labs = model_lab.query.all()
        return jsonify(all_labs)
