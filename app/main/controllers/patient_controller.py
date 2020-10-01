import json

from flask_restx import Resource, Namespace
from flask import jsonify, flash
from sqlalchemy.exc import SQLAlchemyError
from ..models.patient import Patient as model_patient
from ..util.dto import PatientDto

patient = PatientDto.api

@patient.route('/', methods=['GET'])
class Patient(Resource):
    def get(self):
        """Query all patient information"""
        all_patients = model_patient.query.all()
        # result = patient.patients_schema.dump(all_patients)
        return jsonify(all_patients)

@patient.route('/page/<int:page>', methods=['GET'])
class Patient(Resource):
    def get(self, page):
        """pagination route patient information"""
        try:
            patients_list =  model_patient.query.order_by(
                model_patient.id.asc()
            ).paginate(page, per_page=5)

            list_item =[]
            for row in patients_list.items:
                list_item.append(row.serialize())

        except SQLAlchemyError:
            flash("No data in database")
            patients_list = None

        return jsonify({'limit': page, 'search_result': list_item})