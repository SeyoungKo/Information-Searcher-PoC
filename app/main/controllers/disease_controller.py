from flask_restx import Resource, Namespace
from flask import jsonify
from ..models.disease import Disease as model_disease
from ..util.dto import DiseaseDto

disease = DiseaseDto.api

@disease.route('/', methods=['GET'])
class Disease(Resource):
    def get(self):
        """Query all diseases information"""
        all_diseases = model_disease.query.all()
        # result = patient.patients_schema.dump(all_patients)
        return jsonify(all_diseases)

