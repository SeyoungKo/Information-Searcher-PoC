from flask_restx import Resource, Namespace
from flask import jsonify, request, flash
from ..models.disease import Disease as model_disease
from ..util.dto import DiseaseDto
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import select
from sqlalchemy import column, text
import app.main

disease = DiseaseDto.api

@disease.route('/', methods=['GET'])
class Disease(Resource):
    def get(self):
        """Query all diseases information"""
        all_diseases = model_disease.query.all()
        # result = patient.patients_schema.dump(all_patients)
        return jsonify(all_diseases)

@disease.route('/attr/', methods=['GET'])
class Disease(Resource):
    def get(self):
        """Using Dynamic queries with disease information"""
        query_string = request.args.getlist('attributes')
        try:
            stmt = select([column(q) for q in query_string]).\
                select_from(text('disease'))
            print(stmt)
            app.main.db.session.query()

            results = app.main.db.session.execute(stmt).fetchall()

        except SQLAlchemyError:
            flash("No data in database")

        return jsonify({'search_result': [dict(row) for row in results]})

@disease.route('/page/<int:offset>/<int:limit>', methods=['GET'])
class Disease(Resource):
    def get(self, offset, limit):
        """pagination route disease information"""
        try:
            diseases_list =  model_disease.query.order_by(
                model_disease.id.asc()
            ).paginate(offset, per_page=limit)

            list_item =[]
            for row in diseases_list.items:
                list_item.append(row.serialize())

        except SQLAlchemyError:
            flash("No data in database")
            diseases_list = None

        return jsonify({'offset': offset, 'limit':limit, 'search_result': list_item})
