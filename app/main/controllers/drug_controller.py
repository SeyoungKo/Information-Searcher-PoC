from flask_restx import Resource, Namespace
from flask import jsonify, flash, request
from sqlalchemy import column, text
from sqlalchemy.exc import SQLAlchemyError
from ..models.drug import Drug as model_drug
from ..util.dto import DrugDto
from sqlalchemy.sql import select
import app.main

drug = DrugDto.api

@drug.route('/', methods=['GET'])
class Drug(Resource):
    def get(self):
        """Query all drug information"""
        all_drugs = model_drug.query.all()
        # result = patient.patients_schema.dump(all_patients)
        return jsonify(all_drugs)

@drug.route('/attr/', methods=['GET'])
class Drug(Resource):
    def get(self):
        """Using Dynamic queries with drug information"""
        query_string = request.args.getlist('attributes')
        try:
            stmt = select([column(q) for q in query_string]).\
                select_from(text('drug'))
            print(stmt)
            app.main.db.session.query()

            results = app.main.db.session.execute(stmt).fetchall()

        except SQLAlchemyError:
            flash("No data in database")

        return jsonify({'attributes': [attr for attr in query_string], 'search_result': [dict(row) for row in results]})

@drug.route('/page/<int:offset>/<int:limit>', methods=['GET'])
class Drug(Resource):
    def get(self, offset, limit):
        """pagination route drug information"""
        try:
            drugs_list =  model_drug.query.order_by(
                model_drug.id.asc()
            ).paginate(offset, per_page=limit)

            list_item =[]
            for row in drugs_list.items:
                list_item.append(row.serialize())

        except SQLAlchemyError:
            flash("No data in database")
            drugs_list = None

        return jsonify({'offset': offset, 'limit':limit, 'search_result': list_item})
