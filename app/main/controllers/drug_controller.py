from flask_restx import Resource, Namespace
from flask import jsonify
from ..models.drug import Drug as model_drug
from ..util.dto import DrugDto

drug = DrugDto.api

@drug.route('/', methods=['GET'])
class Drug(Resource):
    def get(self):
        """Query all drug information"""
        all_drugs = model_drug.query.all()
        # result = patient.patients_schema.dump(all_patients)
        return jsonify(all_drugs)

