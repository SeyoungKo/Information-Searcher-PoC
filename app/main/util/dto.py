from flask_restx import Namespace, fields

class PatientDto:
    api = Namespace('patient', description='patient operation')
    patient = api.model('patient',{
        'first_name' : fields.String(required=False),
        'last_name' : fields.String(required=False),
        'email' : fields.String(required=False),
        'gender' : fields.String(required=False),
        'birthday' : fields.DateTime(required=False)
    })

