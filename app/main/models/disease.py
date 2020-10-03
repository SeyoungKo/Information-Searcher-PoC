from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
import app.main

@dataclass()
class Disease(app.main.db.Model):
    id : int
    disease_code : str
    disease_name : str
    diagnosis_datetime : str
    patient_id : int
    visit_id : int

    __tablename__ = 'disease'
    id = Column(app.main.db.Integer, primary_key=True)
    disease_code = Column(app.main.db.String(50), unique=False)
    disease_name = Column(app.main.db.String(1000), unique=False)
    diagnosis_datetime = Column(app.main.db.DateTime)
    patient_id = Column(app.main.db.Integer, unique=True)
    visit_id = Column(app.main.db.Integer, unique=True)

    def serialize(self):
        return dict(
            id=self.id,
            disease_code=self.disease_code,
            disease_name=self.disease_name,
            diagnosis_datetime=self.diagnosis_datetime,
            patient_id=self.patient_id,
            visit_id=self.visit_id
        )


class DiseaseSchema(app.main.ma.Schema):
    fields = ('disease_code', 'disease_name', 'diagnosis_datetime', 'patient_id', 'visit_id')


disease_schema = DiseaseSchema()
diseases_schema = DiseaseSchema(many=True)

