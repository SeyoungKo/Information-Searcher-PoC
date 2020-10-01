from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
import app.main

@dataclass
class Visit(app.main.db.Model):
    id: int
    visit_type: str
    admit_datetime: str
    length_of_stay: int
    department: str
    patient_id: int

    __tablename__ = 'visit'
    id = Column(app.main.db.Integer, primary_key=True)
    visit_type = Column(app.main.db.String(3), unique=False)
    admit_datetime = Column(app.main.db.DateTime)
    length_of_stay = Column(app.main.db.Integer, unique=False)
    department = Column(app.main.db.String(50), unique=False)
    patient_id = Column(app.main.db.Integer, unique=False)

