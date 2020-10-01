from flask_restx import Resource, Namespace
from flask import jsonify
from ..models.visit import Visit as model_visit
from ..util.dto import VisitDto

visit = VisitDto.api

@visit.route('/', methods=['GET'])
class Visit(Resource):
    def get(self):
        """Query all visit information"""
        all_visits = model_visit.query.all()
        # result = patient.patients_schema.dump(all_patients)
        return jsonify(all_visits)

