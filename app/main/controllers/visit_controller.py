from flask_restx import Resource, Namespace
from flask import jsonify, flash, request
from sqlalchemy import column, text

from ..models.visit import Visit as model_visit
from ..util.dto import VisitDto
from sqlalchemy.exc import SQLAlchemyError
from ..util.dto import PatientDto
from sqlalchemy.sql import select
import app.main

visit = VisitDto.api

@visit.route('/', methods=['GET'])
class Visit(Resource):
    def get(self):
        """Query all visit information"""
        all_visits = model_visit.query.all()
        # result = patient.patients_schema.dump(all_patients)
        return jsonify(all_visits)

@visit.route('/attr/', methods=['GET'])
class Visit(Resource):
    def get(self):
        """Using Dynamic queries with visit information"""
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

@visit.route('/page/<int:offset>/<int:limit>', methods=['GET'])
class Visit(Resource):
    def get(self, offset, limit):
        """pagination route visit information"""
        try:
            vists_list =  model_visit.query.order_by(
                model_visit.id.asc()
            ).paginate(offset, per_page=limit)

            list_item =[]
            for row in vists_list.items:
                list_item.append(row.serialize())

        except SQLAlchemyError:
            flash("No data in database")
            vists_list = None

        return jsonify({'offset': offset, 'limit':limit, 'search_result': list_item})
