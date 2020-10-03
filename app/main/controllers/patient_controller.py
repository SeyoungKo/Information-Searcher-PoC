from flask_restx import Resource, Namespace
from flask import jsonify, flash, request
from sqlalchemy import column, text
from sqlalchemy.exc import SQLAlchemyError
from ..models.patient import Patient as model_patient
from ..util.dto import PatientDto
from sqlalchemy.sql import select
import app.main

patient = PatientDto.api

@patient.route('/', methods=['GET'])
class PatientAll(Resource):
    def get(self):
        """Query all patient information"""
        all_patients = model_patient.query.all()
        return jsonify(all_patients)

@patient.route('/attr/', methods=['GET'])
class PatientAttr(Resource):

    def get(self):
        """Using Dynamic queries with patient information"""
        query_string = request.args.getlist('attributes')
        try:
            stmt = select([column(q) for q in query_string]).\
                select_from(text('patient'))
            print(stmt)
            app.main.db.session.query()

            results = app.main.db.session.execute(stmt).fetchall()

        except SQLAlchemyError:
            flash("No data in database")

        return jsonify({'search_result': [dict(row) for row in results]})

@patient.route('/page/<int:offset>/<int:limit>', methods=['GET'])
class PatientPaginate(Resource):
    def get(self, offset, limit):
        """pagination route patient information"""
        try:
            patients_list =  model_patient.query.order_by(
                model_patient.id.asc()
            ).paginate(offset, per_page=limit)

            list_item =[]
            for row in patients_list.items:
                list_item.append(row.serialize())

        except SQLAlchemyError:
            flash("No data in database")
            patients_list = None

        return jsonify({'offset': offset, 'limit':limit, 'search_result': list_item})
