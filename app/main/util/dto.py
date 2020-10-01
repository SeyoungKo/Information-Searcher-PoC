from flask_restx import Namespace, fields

class PatientDto:
    api = Namespace('patient', description='relating to patient operation')
    patient = api.model('patient',{
        'first_name' : fields.String(required=False),
        'last_name' : fields.String(required=False),
        'email' : fields.String(required=False),
        'gender' : fields.String(required=False),
        'birthday' : fields.DateTime(required=False)
    })

class DiseaseDto:
    api = Namespace('disease', description='disease operation')
    patient = api.model('disease', {
        'disease_code': fields.String(required=False),
        'disease_name': fields.String(required=False),
        'diagnosis_datetime': fields.DateTime(required=False),
        'patient_id': fields.String(required=False),
        'visit_id': fields.String(required=False)
    })

class DrugDto:
    api = Namespace('drug', description='relating to drug operation')
    drug = api.model('drug', {
        'drug_name': fields.String(required=False),
        'ingredient': fields.String(required=False),
        'order_datetime': fields.DateTime(required=False),
        'drug_company': fields.String(required=False),
        'dose': fields.Integer(required=False),
        'unit': fields.String(required=False),
        'patient_id': fields.Integer(required=False),
        'visit_id': fields.Integer(required=False)
    })

class VisitDto:
    api = Namespace('visit', description='relating to visit operation')
    visit = api.model('visit', {
        'visit_type': fields.String(required=False),
        'admit_datetime': fields.DateTime(required=False),
        'length_of_stay': fields.Integer(required=False),
        'department': fields.String(required=False),
        'patient_id': fields.Integer(required=False)
    })

class LabDto:
    api = Namespace('lab', description='relating to lab operation')
    lab = api.model('lab', {
        'lab_item_code': fields.String(required=False),
        'lab_item_name': fields.String(required=False),
        'charttime': fields.DateTime(required=False),
        'value': fields.Integer(required=False),
        'unit': fields.String(required=False),
        'patient_id' : fields.Integer(required=False),
        'visit_id' : fields.Integer(required=False)
    })
