from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
import app.main
import decimal

@dataclass
class Lab(app.main.db.Model):
    id: int
    lab_item_code: str
    lab_item_name: str
    charttime: str
    value: decimal
    unit: str
    patient_id: int
    visit_id: int

    __tablename__ = 'lab'
    id = Column(app.main.db.Integer, primary_key=True)
    lab_item_code = Column(app.main.db.String(50), unique=False)
    lab_item_name = Column(app.main.db.String(50), unique=False)
    charttime = Column(app.main.db.DateTime)
    value = Column(app.main.db.Numeric(4,2), unique=False)
    unit = Column(app.main.db.String(5), unique=False)
    patient_id = Column(app.main.db.Integer, unique=True)
    visit_id = Column(app.main.db.Integer, unique=True)

    def serialize(self):
        return dict(
            id = self.id,
            lab_item_code = self.lab_item_code,
            lab_item_name = self.lab_item_name,
            charttime = self.charttime,
            value = self.value,
            unit = self.unit,
            patient_id = self.patient_id,
            visit_id = self.visit_id
        )

class LabSchema(app.main.ma.Schema):
    fields = ('lab_item_code', 'lab_item_name', 'charttime', 'value', 'unit', 'patient_id', 'visit_id')

lab_schema = LabSchema()
labs_schema = LabSchema(many=True)
