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

    def __repr__(self):
        return '<disease {}>'.format(self.disease_name)
