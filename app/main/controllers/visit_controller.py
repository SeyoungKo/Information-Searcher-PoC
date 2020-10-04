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
class VisitAll(Resource):
    def get(self):
        """Query all visit information"""
        all_visits = model_visit.query.all()
        return jsonify(all_visits)

@visit.route('/attr/', methods=['GET'])
class VisitAttr(Resource):
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

        return jsonify({'attributes': [attr for attr in query_string], 'search_result': [dict(row) for row in results]})

@visit.route('/page/<int:offset>/<int:limit>', methods=['GET'])
class VisitPaginate(Resource):
    def get(self, offset, limit):
        """Visit information about the pagination route"""
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

        return jsonify({'offset': offset, 'limit': limit, 'search_result': list_item})

@visit.route('/<text>', methods=['GET'])
class VisitFreetext(Resource):
    def get(self, text):
        """Visit information for specific search condition"""
        attr = text
        search_keyword = request.get_json(force=True)[str(attr)]

        model_attr = getattr(model_visit, attr)
        results = model_visit.query.filter(model_attr == search_keyword).all()

        return jsonify({'attributes': attr, 'query': search_keyword, 'results': results})


