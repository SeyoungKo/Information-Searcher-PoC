from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
import app.main

@dataclass
class Drug(app.main.db.Model):
    id: int
    drug_name: str
    ingredient: str
    order_datetime: str
    drug_company: str
    dose: int
    unit : str
    patient_id : int
    visit_id : int

    __tablename__ = 'drug'
    id = Column(app.main.db.Integer, primary_key=True)
    drug_name = Column(app.main.db.String(50), unique=False)
    ingredient = Column(app.main.db.String(50), unique=False)
    order_datetime = Column(app.main.db.DateTime)
    drug_company = Column(app.main.db.String(50), unique=False)
    dose = Column(app.main.db.Integer, unique=False)
    unit= Column(app.main.db.String(3), unique=False)
    patient_id = Column(app.main.db.Integer, unique=True)
    visit_id = Column(app.main.db.Integer, unique=True)

    def serialize(self):
        return dict(
            id = self.id,
            drug_name = self.drug_name,
            ingredient = self.ingredient,
            order_datetime = self.order_datetime,
            drug_company = self.drug_company,
            dose = self.dose,
            unit = self.unit,
            patient_id = self.patient_id,
            visit_id = self.visit_id
        )

class DrugSchema(app.main.ma.Schema):
    fields = ('drug_name', 'ingredient', 'order_datetime', 'drug_company', 'dose', 'unit', 'patient_id', 'visit_id')

drug_schema = DrugSchema()
drugs_schema = DrugSchema(many=True)

