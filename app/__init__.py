from flask_restx import Api
from flask import Blueprint
import app.main
from .main.controllers.patient_controller import api as patient

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          version='1.0',
          title= 'test title',
          description= 'api test description')

api.add_namespace(patient, path='/patients')
