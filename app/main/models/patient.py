from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
import app.main

@dataclass
class Patient(app.main.db.Model):
    id: int
    first_name: str
    last_name: str
    email: str
    gender: str
    birthday: str

    __tablename__ = 'patient'
    id = Column(app.main.db.Integer, primary_key=True)
    first_name = Column(app.main.db.String(50), unique=False)
    last_name = Column(app.main.db.String(50), unique=False)
    email = Column(app.main.db.String(50), unique=False)
    gender = Column(app.main.db.String(50), unique=False)
    birthday = Column(app.main.db.DateTime)

    def serialize(self):
        return dict(
            id = self.id,
            first_name = self.first_name,
            last_name = self.last_name,
            email = self.email,
            gender = self.gender,
            birthday = self.birthday
        )

class PatientSchema(app.main.ma.Schema):
    fields = ('first_name', 'last_name', 'email', 'gender', 'birthday')

patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)
