from flask_restx import Api
from flask import Blueprint
import app.main
from .main.controllers.patient_controller import patient
from .main.controllers.disease_controller import disease
from .main.controllers.visit_controller import visit
from .main.controllers.drug_controller import drug
from .main.controllers.lab_controller import lab

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          version='1.0',
          title= 'Information Searcher API server',
          description= 'Information Searacher api server description')

api.add_namespace(patient, path='/patients')
api.add_namespace(disease, path='/diseases')
api.add_namespace(visit, path='/visits')
api.add_namespace(drug, path='/drugs')
api.add_namespace(lab, path='/labs')