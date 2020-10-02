from flask_restx import Resource, Namespace
from flask import jsonify, request, flash
from ..models.lab import Lab as model_lab
from ..util.dto import LabDto
from sqlalchemy import column, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import select
import app.main

lab = LabDto.api

@lab.route('/', methods=['GET'])
class Lab(Resource):
    def get(self):
        """Query all lab information"""
        all_labs = model_lab.query.all()
        return jsonify(all_labs)

@lab.route('/attr/', methods=['GET'])
class Lab(Resource):
    def get(self):
        """Using Dynamic queries with lab information"""
        query_string = request.args.getlist('attributes')
        try:
            stmt = select([column(q) for q in query_string]).\
                select_from(text('lab'))
            print(stmt)
            app.main.db.session.query()

            results = app.main.db.session.execute(stmt).fetchall()

        except SQLAlchemyError:
            flash("No data in database")

        return jsonify({'search_result': [dict(row) for row in results]})

@lab.route('/page/<int:offset>/<int:limit>', methods=['GET'])
class Lab(Resource):
    def get(self, offset, limit):
        """pagination route lab information"""
        try:
            labs_list =  model_lab.query.order_by(
                model_lab.id.asc()
            ).paginate(offset, per_page=limit)

            list_item =[]
            for row in labs_list.items:
                list_item.append(row.serialize())

        except SQLAlchemyError:
            flash("No data in database")
            labs_list = None

        return jsonify({'offset': offset, 'limit':limit, 'search_result': list_item})
