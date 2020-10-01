from flask_restx import Resource, Namespace
from flask import jsonify
from ..models.patient import Patient as model_patient
import app.main.models.patient as patient
from ..util.dto import PatientDto

patient = PatientDto.api

@patient.route('/', methods=['GET'])
class Patient(Resource):
    def get(self):
        """Query all patient information"""
        all_patients = model_patient.query.all()
        # result = patient.patients_schema.dump(all_patients)
        return jsonify(all_patients)

